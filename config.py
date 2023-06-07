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

        # Endpoint
        self.endpoint = 'http://environment.data.gov.uk/water-quality/{query}'

        # References: API (Application Programming Interface)
        self.Reference_ = collections.namedtuple(
            typename='Reference_', field_names=['code', 'query', 'basename'])

    def references(self) -> ReferenceDirectory:
        """

        :return:
        """

        # The reference data directories.
        directory = self.ReferenceDirectory(
            raw=os.path.join(os.getcwd(), 'data', 'references'),
            structured=os.path.join(os.getcwd(), 'warehouse', 'references'))

        return directory
