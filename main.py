from lib.game import Game
from lib.game.game import MatchParameters
from lib.game.map.builder.static_map_builder import StaticMapBuilder
from lib.view import ConsoleView

if __name__ == '__main__':
    map_builder = StaticMapBuilder()
    game = Game(map_builder)
    game.start(MatchParameters())

    view = ConsoleView()
    while game.is_active():
        game.next_turn()
        game_state = game.get_state()
        view.show(game_state)
