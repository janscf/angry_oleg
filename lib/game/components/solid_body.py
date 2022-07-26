from typing import TYPE_CHECKING

from lib.game.components import Component
from lib.game.components import ComponentState
from lib.game.components import ComponentType
from lib.game.messages.collision_message import CollisionMessage
from lib.game.messages.update_state_message import UpdateStateMessage

if TYPE_CHECKING:
    from lib.game import GameContext
    from lib.game.map import Position
    from lib.game.messages import GameMessage
    from lib.game.objects import GameObject


class SolidBodyState(ComponentState):
    def __init__(self, position: 'Position'):
        super(SolidBodyState, self).__init__(ComponentType.SolidBody)
        self.__position = position

    @property
    def position(self) -> 'Position':
        return self.__position


class SolidBody(Component[SolidBodyState]):
    def __init__(self, owner: 'GameObject'):
        super(SolidBody, self).__init__(owner)

    @property
    def type(self) -> 'ComponentType':
        return ComponentType.SolidBody

    def get_state(self, context: 'GameContext') -> SolidBodyState:
        position = context.map.find_object(self._owner.id)
        return SolidBodyState(position)

    def process_message(self, message: 'GameMessage', context: 'GameContext'):
        if isinstance(message, UpdateStateMessage):
            self.__detect_collisions(context)

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

    # def __move_in_direction(self, direction: 'Direction'):
    #     dx, dy = direction.get_normalized_offset()
    #     current_position = self.get_current_position()
    #     new_position = current_position.increment(dx, dy)
    #     self.__map.place_object(self.owner, new_position)
