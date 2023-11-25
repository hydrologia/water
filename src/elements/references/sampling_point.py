"""
sampling_point.py
"""
import os

import pandas as pd

import config
import src.functions.streams
import src.interface.integrity
import src.configuration.references


class SamplingPoint:
    """
    Class SamplingPoint
    """

    def __init__(self):
        """
        The constructor
        """

        # The reference's default field names, and alternative names
        self.__fields = {'notation': 'sampling_point_id', 'label': 'sampling_point_desc',
                         'comment': 'sampling_point_definition', 'easting': 'easting', 'northing': 'northing',
                         'lat': 'latitude', 'long': 'longitude', 'area.label': 'area_desc',
                         'subArea.label': 'subarea_desc', 'samplingPointType.label': 'sampling_point_type_desc',
                         'samplingPointStatus.label': 'sampling_point_state'}

        # The API parameters of the determinands reference data
        self.__references = src.configuration.references.References().exc(code="sampling_point")

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

    def __structure(self, blob: pd.DataFrame, subarea: pd.DataFrame, sampling_point_types: pd.DataFrame) -> str:
        """

        :param blob: The data in focus
        :param subarea: The subarea reference data
        :param sampling_point_types: The sampling point types reference data
        :return:
        """

        # Focus, rename
        frame: pd.DataFrame = blob.copy()[self.__fields.keys()]
        frame.rename(columns=self.__fields, inplace=True)

        # Subarea
        frame = frame.copy().merge(subarea, how='left', on='subarea_desc')\
            .drop(columns='subarea_desc')

        # Sampling Point Types
        frame = frame.copy().merge(sampling_point_types[['sampling_point_type_id', 'sampling_point_type_desc']],
                                   how='left', on='sampling_point_type_desc')\
            .drop(columns='sampling_point_type_desc')

        # Write
        return self.__write(blob=frame, root=self.__directory.structured)

    def exc(self, subarea: pd.DataFrame, sampling_point_types: pd.DataFrame) -> str:
        """

        :param subarea: The subarea reference data
        :param sampling_point_types: The sampling point types reference data
        :return:
        """

        frame: pd.DataFrame = src.interface.integrity.Integrity().exc(
            affix=self.__references.affix)

        # Keep a copy of the raw data
        self.__write(blob=frame, root=self.__directory.raw)

        # Structure and save
        return self.__structure(blob=frame, subarea=subarea, sampling_point_types=sampling_point_types)
