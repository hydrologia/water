import yaml
import os

import config


class References:

    """
    Class Connector
    """

    def __init__(self):
        """
        Constructor
        """

        # The expected location of the YAML
        self.__path = os.path.join(os.getcwd(), 'resources', 'references.yaml')

        # Get the stream of database credentials as soon as this class is instantiated
        self.__stream = self.__get_stream()

    def __get_stream(self) -> dict:
        """
        Reads the YAML file of database objects. Each object being the set of connection parameters
        of a database.

        :return:
        """

        with open(file=self.__path, mode='r') as stream:
            try:
                return yaml.load(stream=stream, Loader=yaml.CLoader)
            except yaml.YAMLError as err:
                raise Exception(err)

    @staticmethod
    def __excerpt(stream: dict, code: str) -> config.Config().Reference_:
        """
        Extracts the details of an API (Application Programming Interface) object.

        :param stream: A stream of objects wherein each object has the API details for a data set
        :param code: The code of the API object of interest.
        :return:
        """

        # the dictionary of keys in focus
        dictionary: dict = [item for item in stream['nodes'] if item['code'] == code][0]

        # the named tuple form of the keys
        excerpt = config.Config().Reference_(**dictionary)

        return excerpt

    def exc(self, code: str) -> config.Config().Reference_:

        return self.__excerpt(self.__stream, code)
