import os

import pandas as pd

import config
import src.functions.streams
import src.interface.measures
import src.interface.references


class SamplingPointTypes:

    def __init__(self):
        """

        """

        # The reference's default field names, and alternative names
        self.__fields = {'notation': 'sampling_point_type_id', 'label': 'sampling_point_type_desc',
                         'group': 'group', 'group_label': 'group_desc'}

        # The API parameters of the determinands reference data
        self.__references = src.interface.references.References().exc(code="sampling_point_types")

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

        # Focus, rename
        frame: pd.DataFrame = blob.copy()[self.__fields.keys()]
        frame.rename(columns=self.__fields, inplace=True)

        self.__write(blob=frame, root=self.__directory.structured)

    def exc(self):
        """

        :return:
        """

        frame: pd.DataFrame = src.interface.measures.Measures().exc(
            query=self.__references.query)

        # Keep a copy of the raw data
        self.__write(blob=frame, root=self.__directory.raw)

        # Structure and save
        self.__structure(blob=frame)
