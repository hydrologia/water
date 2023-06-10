"""
measures.py
"""
import logging
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

        logging.basicConfig(level=logging.INFO, format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

        # The environment agency's water quality API (Application Programming Interface) endpoint
        configurations = config.Config()
        self.__endpoint = configurations.endpoint

    @staticmethod
    def __read(url, usecols: list = None) -> pd.DataFrame:
        """

        :param url:
        :return:
        """

        response = requests.get(url=url, timeout=900)

        try:
            if response.status_code == 200:
                frame = pd.read_csv(filepath_or_buffer=url, usecols=usecols)
            else:
                frame = pd.DataFrame()
        except RuntimeError as err:
            raise Exception(err)

        return frame

    def exc(self, affix: str = '', query: str = '', usecols: list = None) -> pd.DataFrame:
        """

        :return:
        """

        url = self.__endpoint.format(affix=affix, query=query)
        self.__logger.info(url)

        return self.__read(url=url, usecols=usecols)
