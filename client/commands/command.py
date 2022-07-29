from abc import ABC
from abc import abstractmethod
from typing import Any
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from client.game_client import GameClient


class Command(ABC):
    def __init__(self, client: 'GameClient'):
        self._client = client

    @abstractmethod
    def execute(self, parameter: Any):
        raise NotImplementedError('Not implemented')
