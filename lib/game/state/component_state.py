from abc import ABC
from abc import abstractmethod

from lib.game.enums import ComponentType


class ComponentState(ABC):
    @abstractmethod
    def __init__(self, component_type: 'ComponentType'):
        self.__component_type = component_type

    @property
    def component_type(self) -> 'ComponentType':
        return self.__component_type
