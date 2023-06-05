"""
determinands.py
"""
import config
import src.interface.measures


class Determinands:
    """
    Class Determinands
        Structures the chemical determinands data
    """

    # This is an odd set-up, the normal approach, i.e., setting-up
    # within __init__(), fails.
    configurations = config.Config()
    query = configurations.reference_query

    def __init__(self):
        """

        :return:
        """

        self.__fields = ['notation', 'label', 'definition', 'unit.label', 'unit.comment']

    def exc(self):
        """

        :return:
        """

        frame = src.interface.measures.Measures().exc(branch=self.query.determinands)
        frame = frame.copy()[self.__fields]
        frame.info()
