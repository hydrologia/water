import config
import src.algorithms.references.determinands
import src.functions.directories


class Interface:

    def __init__(self):
        """

        """

        configurations = config.Config()
        _, self.directory = configurations.references()
        paths = list(self.directory)

        directories = src.functions.directories.Directories()
        for path in paths:
            directories.cleanup(path)
            directories.create(path)

    @staticmethod
    def exc():
        """

        :return:
        """

        src.algorithms.references.determinands.Determinands().exc()
