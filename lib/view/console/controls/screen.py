import os


class Screen:
    @staticmethod
    def display(text: str):
        print(text)

    @staticmethod
    def clear_console():
        command = 'clear'
        if os.name in ('nt', 'dos'):
            command = 'cls'
        os.system(command)
