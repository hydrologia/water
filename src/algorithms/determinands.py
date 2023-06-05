"""
determinands.py
"""
import config
import src.interface.measures


class Determinands:
    """
    Class Determinands

    Structures the chemical determinands data.
    """

    def __init__(self):
        """

        :return:
        """

        configurations = config.Config()
        self.query = configurations.reference_query

        self.__fields = ['notation', 'label', 'definition', 'unit.label', 'unit.comment']

    def exc(self):
        """

        :return:
        """

        frame = src.interface.measures.Measures().exc(branch=self.query.determinands)
        frame = frame.copy()[self.__fields]
        frame.info()
