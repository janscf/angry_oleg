from dataclasses import dataclass
from enum import Enum
from enum import auto
from typing import Iterable
from typing import Optional
from typing import TYPE_CHECKING

from lib.game.components import Component
from lib.game.components import ComponentState
from lib.game.components import ComponentType
from lib.game.messages.update_state_message import UpdateStateMessage

if TYPE_CHECKING:
    from lib.game.map import Direction
    from lib.game.messages import GameMessage
    from lib.game.objects import GameObject
    from lib.game.objects import GameObjectType


class SignalLevel(Enum):
    High = auto()
    Average = auto()
    Low = auto()


@dataclass(frozen=True)
class TargetDescriptor:
    direction: 'Direction'
    signal_level: 'SignalLevel'


class DetectorState(ComponentState):
    def __init__(self, targets: Iterable[TargetDescriptor]):
        super(DetectorState, self).__init__(ComponentType.Detector)
        self.__targets = targets

    @property
    def targets(self):
        return self.__targets


class Detector(Component):
    HIGH_SIGNAL_RANGE: int = 7
    AVERAGE_SIGNAL_RANGE: int = 12
    LOW_SIGNAL_RANGE: int = 20

    def __init__(self, owner: 'GameObject', target_type: 'GameObjectType'):
        super(Detector, self).__init__(owner=owner)
        self.__target_type = target_type
        self.__targets = []

    @property
    def type(self) -> 'ComponentType':
        return ComponentType.Detector

    def get_state(self) -> 'ComponentState':
        return DetectorState(targets=self.__targets)

    def process_message(self, message: 'GameMessage'):
        if isinstance(message, UpdateStateMessage):
            self.__find_targets()

    def __find_targets(self):
        self.__targets.clear()
        game_map = self._owner.game_context.map
        for game_object in game_map.get_objects_by_type(self.__target_type):
            distance = game_map.get_distance(self._owner.id, game_object.id)
            signal = self.__get_signal_level(distance)
            if signal:
                direction = game_map.get_direction(self._owner.id, game_object.id)
                self.__targets.append(
                    TargetDescriptor(
                        direction=direction,
                        signal_level=signal,
                    )
                )

    def __get_signal_level(self, distance: float) -> Optional[SignalLevel]:
        if distance > self.LOW_SIGNAL_RANGE:
            return None
        if distance > self.AVERAGE_SIGNAL_RANGE:
            return SignalLevel.Low
        elif distance > self.HIGH_SIGNAL_RANGE:
            return SignalLevel.Average
        return SignalLevel.High
