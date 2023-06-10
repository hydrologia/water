import numpy as np
import pandas as pd
import dask
import config
import os

import src.interface.integrity
import src.functions.streams


class Measurements:

    def __init__(self, sampled_material_types: pd.DataFrame, purposes: pd.DataFrame):
        """

        :param sampled_material_types:
        :param purposes:
        """

        self.__sampled_material_types = sampled_material_types

        self.__purposes = purposes

        self.__affix = '/data/measurement.csv'

        self.__fields = {'determinand.notation': 'determinand_id', 'sample.sampleDateTime': 'datetime',
                         'result': 'measure', 'determinand.unit.label': 'unit_of_measure',
                         'sample.samplingPoint.notation': 'sampling_point_id',
                         'sample.samplingPoint.easting': 'easting', 'sample.samplingPoint.northing': 'northing',
                         'sample.sampledMaterialType.label': 'sampled_material_type_desc',
                         'sample.isComplianceSample': 'is_compliance_sample',
                         'sample.purpose.label': 'purpose_desc'}

        self.__streams = src.functions.streams.Streams()

        self.__pathstr = os.path.join(os.getcwd(), 'warehouse', 'integrity', '{year}', '{area}.csv')

    @dask.delayed
    def __query(self, area: str, year: int) -> str:

        query = f'area={area}&isComplianceSample=false&year={year}'

        return query

    @dask.delayed
    def __readings(self, query: str) -> pd.DataFrame:

        return src.interface.integrity.Integrity().exc(affix=self.__affix, query=query)

    def __rename(self, blob: pd.DataFrame) -> pd.DataFrame:

        return blob.rename(columns=self.__fields)

    @dask.delayed
    def __structure(self, blob: pd.DataFrame) -> pd.DataFrame:
        """

        :param blob:
        :return:
        """

        initial = blob.merge(self.__sampled_material_types, how='left', on='sampled_material_type_desc')\
            .drop(columns='sampled_material_type_desc')

        return initial.merge(self.__purposes, how='left', on='purpose_desc')\
            .drop(columns='purpose_desc')

    @dask.delayed
    def __write(self, blob: pd.DataFrame, year: int, area: str) -> str:
        """

        :param blob:
        :param year:
        :param area:
        :return:
        """

        path = self.__pathstr.format(year=year, area=area)
        return self.__streams.write(data=blob, path=path)

    def exc(self, years: np.ndarray, areas: np.ndarray):
        """

        :return:
        """

        computation = []
        for year in years:

            for area in areas:

                query = self.__query(area=area, year=year)
                readings = self.__readings(query=query)
                renamed = self.__rename(blob=readings)
                structured = self.__structure(blob=renamed)
                message = self.__write(blob=structured, year=year, area=area)

                computation.append(message)

        dask.visualize(computation, filename='integrity', format='pdf')
        calculations = dask.compute(computation, scheduler='threads')[0]

        return calculations
