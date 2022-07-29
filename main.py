from game import Game
from game.objects.player import Player
from service.game_service import GameService
from view import ConsoleView

if __name__ == '__main__':
    game = Game()
    game.start()

    player = Player()
    game.map.place_object_in_random_position(player)
    game.add_player(player.id, '')

    view = ConsoleView(game_service=GameService(game=game))
    while game.is_active():
        game.next_turn()
        game_state = game.get_state()

        view.show(game_state)
