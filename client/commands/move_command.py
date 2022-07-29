from client.commands import Command
from lib.game.enums import Direction


class MoveCommand(Command):

    def execute(self, parameter: 'Direction'):
        self._client.move_to(parameter)
