"""
Module measures.py
"""

import requests
import pandas as pd


class Measures:
    """
    Class Measures

    """

    # This is an odd set-up, the normal approach, i.e., setting-up
    # within __init__(), is failing.
    endpoint: str = 'http://environment.data.gov.uk/water-quality/{branch}'

    def __int__(self):
        """
        The constructor

        :return:
        """

    @staticmethod
    def __read(url) -> pd.DataFrame:
        """

        :param url:
        :return:
        """

        response = requests.get(url=url, timeout=10)

        try:
            if response.status_code == 200:
                frame = pd.read_csv(filepath_or_buffer=url)
            else:
                frame = pd.DataFrame()
        except RuntimeError as err:
            raise Exception(err)

        return frame

    def exc(self, branch: str) -> pd.DataFrame:
        """

        :return:
        """

        url = self.endpoint.format(branch=branch)

        return self.__read(url)
