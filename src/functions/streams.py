"""
Module: streams
"""
import csv
import pathlib

import pandas as pd


class Streams:
    """
    For writing and reading data frames
    """

    def __init__(self):
        """
        """

    @staticmethod
    def write(data: pd.DataFrame, path: str) -> str:
        """
        :param data:
        :param path:
        :return:
        """

        name = pathlib.Path(path).stem

        if data.empty:
            return f'{name}: empty'

        try:
            data.to_csv(path_or_buf=path, index=False, header=True, encoding='utf-8',
                        quoting=csv.QUOTE_NONNUMERIC)
            return f'{name}: succeeded'
        except OSError as err:
            raise Exception(err.strerror) from err

    @staticmethod
    def read(url, header: int = 0, usecols: list = None) -> pd.DataFrame:
        """

        :param url:
        :param header:
        :param usecols:
        :return:
        """

        try:
            return pd.read_csv(filepath_or_buffer=url, header=header, usecols=usecols, encoding='utf-8')
        except ImportError as err:
            raise Exception(err)
