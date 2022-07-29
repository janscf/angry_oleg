from typing import Any

from client.commands import Command


class NextTurnCommand(Command):
    def execute(self, parameter: Any):
        self._client.go_next_turn()
