"""
determinands.py
"""
import os
import pandas as pd

import config
import src.interface.measures
import src.functions.streams
import src.interface.references


class Determinands:
    """
    Class Determinands

    Structures the chemical determinands data.
    """

    def __init__(self):
        """

        :return:
        """

        references = src.interface.references.References()
        self.__references_ = references.exc(code="determinands")

        # The reference's default field names, and alternative names
        self.__fields = {'notation': 'determinand_id', 'label': 'determinand_desc', 'definition': 'definition',
                         'unit.label': 'unit_of_measure', 'unit.comment': 'unit_of_measure_desc'}

        # Writing
        self.__streams = src.functions.streams.Streams()

        # self.__directory hosts the directory names for raw & structured reference data.
        configurations = config.Config()
        self.__directory = configurations.references()

    def __write(self, blob: pd.DataFrame, root: str):

        self.__streams.write(data=blob, path=os.path.join(root, f'{self.__references_.code}.csv'))
        
    def __structure(self, blob: pd.DataFrame):
        
        # structured
        frame: pd.DataFrame = blob.copy()[self.__fields.keys()]
        frame.rename(columns=self.__fields, inplace=True)
        
        self.__write(blob=frame, root=self.__directory.structured)
        
    def exc(self):
        """

        :return:
        """

        frame: pd.DataFrame = src.interface.measures.Measures().exc(
            query=self.__references_.query)

        # Hence
        self.__write(blob=frame, root=self.__directory.raw)
        self.__structure(blob=frame)
