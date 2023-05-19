import logging
import os
import sys


def main():
    """
    The entry point.

    :return:
    """

    logger.info('water')


if __name__ == '__main__':
    root = os.getcwd()
    sys.path.append(root)

    # Logging
    logging.basicConfig(level=logging.INFO,
                        format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(__name__)

    main()
