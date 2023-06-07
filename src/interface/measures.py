"""
Module measures.py
"""

import requests
import pandas as pd

import config


class Measures:
    """
    Class Measures

    """

    def __init__(self):
        """
        The constructor

        :return:
        """

        configurations = config.Config()
        self.__endpoint = configurations.endpoint

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

    def exc(self, query: str) -> pd.DataFrame:
        """

        :return:
        """

        url = self.__endpoint.format(query=query)

        return self.__read(url)
