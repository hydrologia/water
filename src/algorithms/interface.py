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

        configurations = config.Config()

        # Streams
        self.__streams = src.functions.streams.Streams()

        # The water integrity data, and hydrological data, warehouse paths
        self.__integrity = os.path.join(os.getcwd(), 'warehouse', 'integrity', '{year}')

        # Prepare directories
        self.__years = configurations.years
        self.__directories = src.functions.directories.Directories()

    def __areas(self) -> np.ndarray:

        filepath = os.path.join(os.getcwd(), 'warehouse', 'references', 'environment_agency_area.csv')
        return self.__streams.read(url=filepath, usecols=['area_id']).array

    def __sampled_material_types(self) -> pd.DataFrame:

        filepath = os.path.join(os.getcwd(), 'warehouse', 'references', 'sampled_material_types.csv')
        return self.__streams.read(url=filepath,
                                   usecols=['sampled_material_type_id', 'sampled_material_type_desc'])

    def __purposes(self) -> pd.DataFrame:

        filepath = os.path.join(os.getcwd(), 'warehouse', 'references', 'purposes.csv')
        return self.__streams.read(url=filepath,
                                   usecols=['purpose_id', 'purpose_desc'])

    def exc(self):

        [dask.delayed(self.__directories.cleanup)(self.__integrity.format(year=year)) for year in self.__years]
        [dask.delayed(self.__directories.create)(self.__integrity.format(year=year)) for year in self.__years]

        # src.algorithms.measurements.Measurements().exc()






