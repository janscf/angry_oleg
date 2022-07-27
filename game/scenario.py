from abc import ABC
from abc import abstractmethod


class Scenario(ABC):
    @abstractmethod
    def check_condition(self):
        raise NotImplementedError('Not implemented')
