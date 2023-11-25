"""
sampling_point_types.py
"""
import os

import pandas as pd

import config
import src.functions.streams
import src.interface.integrity
import src.configuration.references


class SamplingPointTypes:
    """
    Class SamplingPointTypes
    """

    def __init__(self):
        """
        The constructor
        """

        # The reference's default field names, and alternative names
        self.__fields = {'notation': 'sampling_point_type_id', 'label': 'sampling_point_type_desc',
                         'group': 'group', 'group.label': 'group_desc'}

        # The API parameters of the sampling point types reference data
        self.__references = src.configuration.references.References().exc(code="sampling_point_types")

        # Writing
        self.__streams = src.functions.streams.Streams()

        # self.__directory hosts the directory names for raw & structured reference data.
        configurations = config.Config()
        self.__directory = configurations.references()

    def __write(self, blob: pd.DataFrame, root: str) -> str:
        """

        :param blob: The data being stored
        :param root: The storage directory
        :return:
        """

        return self.__streams.write(data=blob, path=os.path.join(root, f'{self.__references.basename}'))

    def __structure(self, blob: pd.DataFrame) -> pd.DataFrame:
        """

        :param blob: The data in focus
        :return:
        """

        # Focus, rename
        frame: pd.DataFrame = blob.copy()[self.__fields.keys()]
        frame.rename(columns=self.__fields, inplace=True)

        # Codes
        frame.loc[:, 'group'] = frame['group'].apply(lambda x: os.path.basename(x)).array

        # Write
        self.__write(blob=frame, root=self.__directory.structured)

        # Hence
        return frame

    def exc(self) -> pd.DataFrame:
        """

        :return:
        """

        frame: pd.DataFrame = src.interface.integrity.Integrity().exc(
            affix=self.__references.affix)

        # Keep a copy of the raw data
        self.__write(blob=frame, root=self.__directory.raw)

        # Structure and save
        return self.__structure(blob=frame)
