import src.interface.measures


class Determinands:

    def __int__(self, branch="def/determinands.csv"):
        """

        :param branch:
        :return:
        """

        self.branch = branch

    def exc(self):
        """

        :return:
        """

        frame = src.interface.measures.Measures().exc(branch=self.branch)
        frame.info()
