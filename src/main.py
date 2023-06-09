"""
main.py
"""
import logging
import os
import sys


def main():
    """
    The entry point.

    :return:
    """

    logger.info('water')
    src.algorithms.references.interface.Interface().exc()


if __name__ == '__main__':
    root = os.getcwd()
    sys.path.append(root)
    sys.path.insert(0, os.path.join(root, 'src'))

    # Threads
    os.environ['NUMEXPR_MAX_THREADS'] = '8'

    # Logging
    logging.basicConfig(level=logging.INFO, format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(__name__)

    # Classes
    import src.algorithms.references.interface

    main()
