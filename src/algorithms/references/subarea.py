import os

import pandas as pd

import config
import src.functions.streams
import src.interface.measures
import src.interface.references


class Subarea:
    """

    """

    def __init__(self):
        """

        """

        # The reference's default field names, and alternative names
        self.__fields = {'notation': 'subarea_id', 'label': 'subarea_desc',
                         'subOrganizationOf': 'area_id'}

        # The API parameters of the determinands reference data
        self.__references = src.interface.references.References().exc(code="environment_agency_subarea")

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

    def __structure(self, blob: pd.DataFrame) -> pd.DataFrame:
        """

        :param blob:
        :return:
        """

        # Focus, rename
        frame: pd.DataFrame = blob.copy()[self.__fields.keys()]
        frame.rename(columns=self.__fields, inplace=True)

        # Codes
        frame.loc[:, 'area_id'] = frame['area_id'].apply(lambda x: os.path.basename(x)).array

        # Write
        self.__write(blob=frame, root=self.__directory.structured)

        # Hence
        return frame

    def exc(self) -> pd.DataFrame:
        """

        :return:
        """

        frame: pd.DataFrame = src.interface.measures.Measures().exc(
            affix=self.__references.affix)

        # Keep a copy of the raw data
        self.__write(blob=frame, root=self.__directory.raw)

        # Structure and save
        return self.__structure(blob=frame)
