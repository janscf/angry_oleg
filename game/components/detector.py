from typing import Optional
from typing import TYPE_CHECKING

from game.components import Component
from game.messages.update_state_message import UpdateStateMessage
from lib.game.enums import ComponentType
from lib.game.enums import SignalLevel
from lib.game.state.components import DetectorState
from lib.game.state.components.detector import TargetSignal

if TYPE_CHECKING:
    from game import GameContext
    from game.messages import GameMessage
    from game.objects import GameObject
    from lib.game.enums import GameObjectType


class Detector(Component[DetectorState]):
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

    def get_state(self, context: 'GameContext') -> DetectorState:
        return DetectorState(targets=self.__targets)

    def process_message(self, message: 'GameMessage', context: 'GameContext'):
        if isinstance(message, UpdateStateMessage):
            self.__find_targets(context)

    def __find_targets(self, context: 'GameContext'):
        self.__targets.clear()
        game_map = context.map
        for game_object in game_map.get_objects_by_type(self.__target_type):
            distance = game_map.get_distance(self._owner.id, game_object.id)
            signal = self.__get_signal_level(distance)
            if signal:
                direction = game_map.get_direction(self._owner.id, game_object.id)
                self.__targets.append(
                    TargetSignal(
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
