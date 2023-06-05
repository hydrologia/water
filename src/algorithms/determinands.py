import src.interface.measures


class Determinands:
    """
    Class Determinands
        Structures the chemical determinands data
    """

    # This is an odd set-up, the normal approach, i.e., setting-up
    # within __init__(), is failing.
    __branch: str = 'def/determinands.csv'

    def __int__(self):
        """

        :return:
        """

    def exc(self):
        """

        :return:
        """

        frame = src.interface.measures.Measures().exc(branch=self.__branch)
        frame.info()
