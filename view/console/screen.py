import os
from typing import List


class Screen:
    @staticmethod
    def display(text: str):
        print(text)

    @staticmethod
    def join(lines: List[str]) -> str:
        return '\n'.join(lines)

    @staticmethod
    def clear_console():
        command = 'clear'
        if os.name in ('nt', 'dos'):
            command = 'cls'
        os.system(command)
