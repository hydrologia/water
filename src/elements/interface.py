"""
interface.py
"""
import os

import numpy as np
import pandas as pd

import config
import src.algorithms.integrity
import src.functions.directories
import src.functions.streams


class Interface:
    """
    Class Interface
    """

    def __init__(self):
        """
        The constructor
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

        [directories.cleanup(self.__pathstr.format(segment=segment, year=year))
         for segment in self.__segments for year in self.__years]
        [directories.create(self.__pathstr.format(segment=segment, year=year))
         for segment in self.__segments for year in self.__years]

    def __areas(self) -> np.ndarray:
        """

        :return:
        """

        filepath = os.path.join(os.getcwd(), 'warehouse', 'references', 'environment_agency_area.csv')
        frame = self.__streams.read(uri=filepath, usecols=['area_id'])
        areas = frame['area_id'].array

        return areas[~areas.isin(['R'])]

    def __sampled_material_types(self) -> pd.DataFrame:
        """

        :return:
        """

        filepath = os.path.join(os.getcwd(), 'warehouse', 'references', 'sampled_material_types.csv')
        return self.__streams.read(uri=filepath,
                                   usecols=['sampled_material_type_id', 'sampled_material_type_desc'])

    def __purposes(self) -> pd.DataFrame:
        """

        :return:
        """

        filepath = os.path.join(os.getcwd(), 'warehouse', 'references', 'purposes.csv')
        return self.__streams.read(uri=filepath,
                                   usecols=['purpose_id', 'purpose_desc'])

    def exc(self):
        """

        :return:
        """

        # Prepare directories
        self.__directories()

        # Water integrity measures
        src.algorithms.integrity.Integrity(
            sampled_material_types=self.__sampled_material_types(), purposes=self.__purposes()) \
            .exc(years=self.__years, areas=self.__areas())
