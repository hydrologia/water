import src.interface.measures

import config


class Determinands:
    """
    Class Determinands
        Structures the chemical determinands data
    """

    # This is an odd set-up, the normal approach, i.e., setting-up
    # within __init__(), is failing.
    # __branch: str = 'def/determinands.csv'
    configurations = config.Config()
    query = configurations.reference_query

    def __int__(self):
        """

        :return:
        """

    def exc(self):
        """

        :return:
        """

        frame = src.interface.measures.Measures().exc(branch=self.query.determinands)
        frame.info()
