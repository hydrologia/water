"""
determinands.py
"""
import pandas as pd

import config
import src.interface.measures


class Determinands:
    """
    Class Determinands

    Structures the chemical determinands data.
    """

    def __init__(self):
        """

        :return:
        """

        configurations = config.Config()
        self.query = configurations.reference_query

        self.__fields = {'notation': 'determinand_id', 'label': 'determinand_desc', 'definition': 'definition',
                         'unit.label': 'unit_of_measure', 'unit.comment': 'unit_of_measure_desc'}

    def exc(self):
        """

        :return:
        """

        frame: pd.DataFrame = src.interface.measures.Measures().exc(branch=self.query.determinands)
        frame: pd.DataFrame = frame.copy()[self.__fields.keys()]
        frame.rename(columns=self.__fields, inplace=True)
        frame.info()
