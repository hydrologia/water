import logging
import os
import sys


def main():
    """
    The entry point.

    :return:
    """

    term = src.algorithms.determinands.Determinands()
    term.exc()


if __name__ == '__main__':

    root = os.getcwd()
    sys.path.append(root)
    sys.path.insert(0, os.path.join(root, 'src'))

    # Logging
    logging.basicConfig(level=logging.INFO,
                        format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(__name__)

    # Strange
    import src.algorithms.determinands

    main()
