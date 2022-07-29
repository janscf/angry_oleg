from typing import TYPE_CHECKING

from game.components import Component
from game.messages import ChangeDirectionMessage
from game.messages.collision_message import CollisionMessage
from game.messages.update_state_message import UpdateStateMessage
from lib.game.enums import ComponentType
from lib.game.state.components import SolidBodyState

if TYPE_CHECKING:
    from game import GameContext
    from lib.game.enums import Direction
    from game.messages import GameMessage
    from game.objects import GameObject


class SolidBody(Component[SolidBodyState]):
    def __init__(self, owner: 'GameObject', direction: 'Direction' = None):
        super(SolidBody, self).__init__(owner)
        self.__direction = direction

    @property
    def type(self) -> 'ComponentType':
        return ComponentType.SolidBody

    def get_state(self, context: 'GameContext') -> SolidBodyState:
        position = context.map.find_object(self._owner.id)
        return SolidBodyState(position=position, direction=self.__direction)

    def process_message(self, message: 'GameMessage', context: 'GameContext'):
        if isinstance(message, UpdateStateMessage):
            self.__move(context, self.__direction)
            self.__detect_collisions(context)
        elif isinstance(message, ChangeDirectionMessage):
            self.__direction = message.new_direction

    def __detect_collisions(self, game_context: 'GameContext'):
        game_map = game_context.map
        current_position = game_map.find_object(self._owner.id)
        objects_in_position = game_map.get_objects_in_position(current_position)
        for existing_object in objects_in_position:
            if existing_object.id == self._owner.id:
                continue

            if not existing_object.has_component(ComponentType.SolidBody):
                continue

            self._owner.send_message(CollisionMessage(existing_object.id))

    def __move(self, game_context: 'GameContext', direction: 'Direction'):
        if direction is None:
            return

        game_map = game_context.map
        current_position = game_map.find_object(self._owner.id)
        dx, dy = direction.get_normalized_offset()
        new_position = current_position.increment(dx, dy)
        if game_map.is_valid_position(new_position):
            game_map.place_object(self._owner, new_position)
