import logging

FORMAT = '%(asctime)-15s %(message)s'


def init_logging():
    logging.basicConfig(format=FORMAT, level=logging.DEBUG)
