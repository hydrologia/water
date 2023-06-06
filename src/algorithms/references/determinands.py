"""
determinands.py
"""
import os
import pandas as pd

import config
import src.interface.measures
import src.functions.streams


class Determinands:
    """
    Class Determinands

    Structures the chemical determinands data.
    """

    def __init__(self):
        """

        :return:
        """

        # self.__query hosts the query string for retrieving determinands data via the environment
        # agency's API (application programming interface)
        configurations = config.Config()
        self.__query = configurations.reference_query
        self.__directory = configurations.reference_directory

        # Focus
        self.__focus = 'determinands'

        # The reference's default field names, and alternative names
        self.__fields = {'notation': 'determinand_id', 'label': 'determinand_desc', 'definition': 'definition',
                         'unit.label': 'unit_of_measure', 'unit.comment': 'unit_of_measure_desc'}

    def __raw(self, blob: pd.DataFrame):

        src.functions.streams.Streams().write(data=blob, path=os.path.join(self.__directory.raw, f'{self.__focus}.csv'))

    def exc(self):
        """

        :return:
        """

        print(self.__query.__getattribute__(self.__focus))

        frame: pd.DataFrame = src.interface.measures.Measures().exc(branch=self.__query.determinands)
        frame: pd.DataFrame = frame.copy()[self.__fields.keys()]
        frame.rename(columns=self.__fields, inplace=True)
        frame.info()
