import numpy as np
import pandas as pd
import dask
import config
import os

import src.interface.measures
import src.functions.streams


class Measurements:

    def __init__(self):
        """

        """

        configurations = config.Config()
        self.__years = configurations.years

        self.__affix = '/data/measurement.csv'

        self.__fields = {'determinand.notation': 'determinand_id', 'sample.sampleDateTime': 'datetime',
                         'result': 'measure', 'determinand.unit.label': 'unit_of_measure',
                         'sample.samplingPoint.notation': 'sampling_point_id',
                         'sample.samplingPoint.easting': 'easting', 'sample.samplingPoint.northing': 'northing',
                         'sample.sampledMaterialType.label': 'sampled_material_type_desc',
                         'sample.isComplianceSample': 'is_compliance_sample',
                         'sample.purpose.label': 'purpose_desc'}

        self.__streams = src.functions.streams.Streams()

    @staticmethod
    def __areas() -> np.ndarray:

        filepath = os.path.join(os.getcwd(), 'warehouse', 'references', 'environment_agency_area.csv')

        try:
            values = pd.read_csv(filepath_or_buffer=filepath, header=0, encoding='utf-8', usecols='area_id').array
        except ImportError as err:
            raise Exception(err) from err

        return values

    @dask.delayed
    def __query(self, area: str, year: int) -> str:

        query = f'area={area}&isComplianceSample=false&year={year}'

        return query

    @dask.delayed
    def __readings(self, query: str) -> pd.DataFrame:

        return src.interface.measures.Measures().exc(affix=self.__affix, query=query)

    @dask.delayed
    def __structure(self, blob: pd.DataFrame):
        """

        :param blob:
        :return:
        """

    @dask.delayed
    def __write(self, blob: pd.DataFrame, path: str):

        self.__streams.write(data=blob, path=path)

    def exc(self):
        """

        :return:
        """

        computation = []
        for year in self.__years:

            for area in self.__areas():

                query = self.__query(area=area, year=year)

                readings = self.__readings(query=query)
