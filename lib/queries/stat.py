import abc
import logging
import time
from contextlib import contextmanager


class StatCollector(abc.ABC):
    @abc.abstractmethod
    def enter(self, query):
        pass

    @abc.abstractmethod
    def leave(self, query):
        pass

    @contextmanager
    def track(self, query):
        self.enter(query)
        yield
        self.leave(query)



class LogStatCollector(StatCollector):
    start: float
    logger: logging.Logger

    def enter(self, query):
        self.logger = logging.getLogger(query.name)
        self.logger.info('beginning query %s execution', query.name)
        self.start = time.time()

    def leave(self, query):
        took = time.time() - self.start
        self.logger.info('query %s execution finished. took %s', query.name, took)
