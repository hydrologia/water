"""
interface.py
"""
import pandas as pd

import config
import src.algorithms.references.determinands
import src.algorithms.references.purposes
import src.algorithms.references.sampled_material_types
import src.functions.directories

import src.algorithms.references.area
import src.algorithms.references.subarea
import src.algorithms.references.sampling_point_types
import src.algorithms.references.sampling_point


class Interface:
    """
    Class Interface

    Runs all the reference data extraction programs
    """

    def __init__(self):
        """

        """

        configurations = config.Config()
        self.directory = configurations.references()
        paths = list(self.directory)

        directories = src.functions.directories.Directories()
        for path in paths:
            directories.cleanup(path)
            directories.create(path)

    @staticmethod
    def exc():
        """

        :return:
        """

        src.algorithms.references.area.Area().exc()
        src.algorithms.references.determinands.Determinands().exc()
        src.algorithms.references.purposes.Purposes().exc()
        src.algorithms.references.sampled_material_types.SamplingMaterialTypes().exc()
        sampling_point_types: pd.DataFrame = src.algorithms.references.sampling_point_types.SamplingPointTypes().exc()
        subarea: pd.DataFrame = src.algorithms.references.subarea.Subarea().exc()

        src.algorithms.references.sampling_point.SamplingPoint().exc(
            subarea=subarea, sampling_point_types=sampling_point_types)
