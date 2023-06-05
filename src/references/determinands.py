import src.interface.measures


class Determinands:
    def __int__(self, branch: str = 'def/determinands.csv'):
        """

        :return:
        """

        self.__branch = branch

    def exc(self):
        """

        :return:
        """

        frame = src.interface.measures.Measures().exc(branch=self.__branch)
        frame.info()
