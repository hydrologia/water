"""
sampled_material_types.py
"""
import os

import pandas as pd

import config
import src.functions.streams
import src.interface.integrity
import src.configuration.references


class SamplingMaterialTypes:
    """
    Class SamplingMaterialTypes
    """

    def __init__(self):
        """
        The constructor
        """

        # The reference's default field names, and alternative names
        self.__fields = {'notation': 'sampled_material_type_id', 'label': 'sampled_material_type_desc'}

        # The API parameters of the sampled material type reference data
        self.__references = src.configuration.references.References().exc(code="sampled_material_types")

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

    def __structure(self, blob: pd.DataFrame) -> str:
        """

        :param blob: The data in focus
        :return:
        """

        # Rename
        frame: pd.DataFrame = blob.copy()
        frame.rename(columns=self.__fields, inplace=True)

        # Ascertain upper case; initially strip.
        frame.loc[:, 'sampled_material_type_id'] = frame['sampled_material_type_id'].str.strip().str.upper().array

        # Write
        return self.__write(blob=frame, root=self.__directory.structured)

    def exc(self) -> str:
        """

        :return: Data extraction, structuring, and storage message
        """

        frame: pd.DataFrame = src.interface.integrity.Integrity().exc(
            affix=self.__references.affix, usecols=list(self.__fields.keys()))

        # Keep a copy of the raw data
        self.__write(blob=frame, root=self.__directory.raw)

        # Structure and save
        return self.__structure(blob=frame)
