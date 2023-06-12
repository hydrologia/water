import os
import logging
import requests
import pandas as pd


class Stations:

    def __init__(self):
        """

        """

        self.__url = 'https://environment.data.gov.uk/hydrology/id/stations.json?_limit=10000'

        # Logging
        logging.basicConfig(level=logging.INFO, format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def __read(self) -> requests.Response:
        """
        An unnecessary double; inspecting.

        :return:
        """

        try:
            response = requests.get(url=self.__url)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise Exception(f'HTTP Error: {err}')
        except Exception as err:
            raise Exception(err) from err

        if response.status_code == 200:
            return response
        else:
            raise Exception(f'Failure code: {response.status_code}')

    @staticmethod
    def __types(nodes):
        """

        :param nodes:
        :return:
        """

        return [os.path.basename(list(node.values())[0])
                for node in nodes]

    def exc(self):
        """
        ['label', 'notation', 'easting', 'northing', 'lat', 'long', 'type']

        :return:
        """

        response = self.__read()
        blob = response.json()
        data = pd.json_normalize(data=blob, record_path='items')
        data.info()

        # Decomposing
        data.loc[:, 'type'] = data['type'].apply(lambda x: self.__types(x))
        self.__logger.info(data[['label', 'notation', 'easting', 'northing', 'type']])
