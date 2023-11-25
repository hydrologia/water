"""
interface.py
"""
import pandas as pd

import config
import src.elements.references.area
import src.elements.references.determinands
import src.elements.references.purposes
import src.elements.references.sampled_material_types
import src.elements.references.sampling_point
import src.elements.references.sampling_point_types
import src.elements.references.subarea
import src.functions.directories


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
    def exc() -> str:
        """

        :return:
        """

        src.elements.references.area.Area().exc()
        src.elements.references.determinands.Determinands().exc()
        src.elements.references.purposes.Purposes().exc()
        src.elements.references.sampled_material_types.SamplingMaterialTypes().exc()
        sampling_point_types: pd.DataFrame = src.elements.references.sampling_point_types.SamplingPointTypes().exc()
        subarea: pd.DataFrame = src.elements.references.subarea.Subarea().exc()

        return src.elements.references.sampling_point.SamplingPoint().exc(
            subarea=subarea, sampling_point_types=sampling_point_types)
