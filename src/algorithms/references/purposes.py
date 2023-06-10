"""
purposes.py
"""
import os

import pandas as pd

import config
import src.functions.streams
import src.interface.integrity
import src.configuration.references


class Purposes:
    """
    Class Purposes
    """

    def __init__(self):
        """
        The constructor
        """

        # The reference's default field names, and alternative names
        self.__fields = {'notation': 'purpose_id', 'label': 'purpose_desc'}

        # The API parameters of the purposes reference data
        self.__references = src.configuration.references.References().exc(code="purposes")

        # Writing
        self.__streams = src.functions.streams.Streams()

        # self.__directory hosts the directory names for raw & structured reference data.
        configurations = config.Config()
        self.__directory = configurations.references()

    def __write(self, blob: pd.DataFrame, root: str):
        """

        :param blob:
        :param root:
        :return:
        """

        self.__streams.write(data=blob, path=os.path.join(root, f'{self.__references.basename}'))

    def __structure(self, blob: pd.DataFrame):
        """

        :param blob:
        :return:
        """

        # Rename
        frame: pd.DataFrame = blob.copy()
        frame.rename(columns=self.__fields, inplace=True)

        # Write
        self.__write(blob=frame, root=self.__directory.structured)

    def exc(self):
        """

        :return:
        """

        frame: pd.DataFrame = src.interface.integrity.Integrity().exc(
            affix=self.__references.affix, usecols=list(self.__fields.keys()))

        # Keep a copy of the raw data
        self.__write(blob=frame, root=self.__directory.raw)

        # Structure and save
        self.__structure(blob=frame)
