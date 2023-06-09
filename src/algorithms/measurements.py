import numpy as np
import pandas as pd
import dask
import config
import os

import src.interface.measures


class Measurements:

    def __init__(self):
        """

        """

        configurations = config.Config()
        self.__years = configurations.years

        self.__affix = '/data/measurement.csv'

        self.__area = os.path.join(os.getcwd(), 'warehouse', 'references', 'environment_agency_area.csv')

    def __areas(self) -> np.ndarray:

        try:
            values = pd.read_csv(filepath_or_buffer=self.__area, header=0, encoding='utf-8', usecols='area_id').array
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

    def exc(self):
        """

        :return:
        """

        computation = []
        for area in self.__areas():

            for year in self.__years:

                query = self.__query(area=area, year=year)

                readings = self.__readings(query=query)
