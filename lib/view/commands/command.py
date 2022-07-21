from abc import ABC
from abc import abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self, parameter):
        raise NotImplementedError('Not implemented')
