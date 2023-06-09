"""
config.py
"""
import collections
import os


class Config:
    """
    The project's global configurations

    """
    ReferenceDirectory = collections.namedtuple(
        typename='ReferenceDirectory', field_names=['raw', 'structured'])

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
        self.years = range(2000, 2024)

    def references(self) -> ReferenceDirectory:
        """

        :return:
        """

        # The reference data directories.
        directory = self.ReferenceDirectory(
            raw=os.path.join(os.getcwd(), 'data', 'references'),
            structured=os.path.join(os.getcwd(), 'warehouse', 'references'))

        return directory
