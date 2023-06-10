import os
import numpy as np
import pandas as pd
import dask

import src.functions.directories
import src.functions.streams
import config
import src.algorithms.measurements


class Interface:

    def __init__(self):
        """

        """

        self.__years = config.Config().years

        # Streams
        self.__streams = src.functions.streams.Streams()

        # The water integrity data, and hydrological data, warehouse paths
        self.__segments = ['integrity']
        self.__pathstr = os.path.join(os.getcwd(), 'warehouse', '{segment}', '{year}')

    def __directories(self):
        """
        Prepare directories

        :return:
        """

        directories = src.functions.directories.Directories()

        for segment in self.__segments:

            cleanup = [dask.delayed(directories.cleanup)(self.__pathstr.format(segment=segment, year=year))
                       for year in self.__years]
            create = [dask.delayed(directories.create)(self.__pathstr.format(segment=segment, year=year))
                      for year in self.__years]

            dask.compute(cleanup, scheduler='threads')
            dask.compute(create, scheduler='threads')

    def __areas(self) -> np.ndarray:
        """

        :return:
        """

        filepath = os.path.join(os.getcwd(), 'warehouse', 'references', 'environment_agency_area.csv')
        return self.__streams.read(url=filepath, usecols=['area_id']).array

    def __sampled_material_types(self) -> pd.DataFrame:
        """

        :return:
        """

        filepath = os.path.join(os.getcwd(), 'warehouse', 'references', 'sampled_material_types.csv')
        return self.__streams.read(url=filepath,
                                   usecols=['sampled_material_type_id', 'sampled_material_type_desc'])

    def __purposes(self) -> pd.DataFrame:
        """

        :return:
        """

        filepath = os.path.join(os.getcwd(), 'warehouse', 'references', 'purposes.csv')
        return self.__streams.read(url=filepath,
                                   usecols=['purpose_id', 'purpose_desc'])

    def exc(self):
        """

        :return:
        """

        # Prepare directories
        self.__directories()

        # Water integrity measures
        src.algorithms.measurements.Measurements(
            sampled_material_types=self.__sampled_material_types(), purposes=self.__purposes())\
            .exc(years=self.__years, areas=self.__areas())
