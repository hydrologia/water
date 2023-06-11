"""
config.py
"""
import collections
import os

import numpy as np


class Config:
    """
    The project's global configurations

    """
    AssetDirectory = collections.namedtuple(
        typename='AssetDirectory', field_names=['raw', 'structured'])

    def __init__(self):
        """

        """

        # The environment agency's default limit is 50
        __limit = '?_limit=1000000'

        # Endpoint
        self.endpoint = 'https://environment.data.gov.uk/water-quality{affix}' + __limit + '{query}'

        # Reference parameters: vis-à-vis environment agency's API (Application Programming Interface)
        # reference data
        self.Reference_ = collections.namedtuple(
            typename='Reference_', field_names=['code', 'affix', 'basename'])

        # Years
        self.years = np.arange(2000, 2009)

    def references(self) -> AssetDirectory:
        """

        :return:
        """

        # The reference data directories.
        directory = self.AssetDirectory(
            raw=os.path.join(os.getcwd(), 'data', 'references'),
            structured=os.path.join(os.getcwd(), 'warehouse', 'references'))

        return directory

    def measurements(self) -> AssetDirectory:

        directory = self.AssetDirectory(
            raw=os.path.join(os.getcwd(), 'data', 'measurements'),
            structured=os.path.join(os.getcwd(), 'warehouse', 'measurements'))

        return directory
