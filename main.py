from client.direct_client import DirectClient
from game import Game
from game.objects.player import Player
from view import ConsoleView

if __name__ == '__main__':
    game = Game()
    game.start()

    player = Player()
    game.map.place_object_in_random_position(player)
    player_descriptor = game.add_player(player.id, '')

    client = DirectClient(player_id=player_descriptor.player_id, game=game)
    view = ConsoleView(game_client=client)
    game.next_turn()
    while game.is_active():
        game_state = game.get_state()
        view.show(game_state)
