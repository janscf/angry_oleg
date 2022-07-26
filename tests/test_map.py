import pytest

from lib.game.exceptions import InvalidWorldSizeException
from lib.game.exceptions import OutOfMapException
from lib.game.map import Map
from lib.game.map import Position
from lib.game.objects.vacuum import Vacuum


def test_create_game_map():
    # Act
    game_map = Map(3, 5)

    assert game_map.size_x == 3
    assert game_map.size_y == 5


def test_create_game_map_with_invalid_size():
    # Act
    with pytest.raises(InvalidWorldSizeException):
        Map(0, 1)

    with pytest.raises(InvalidWorldSizeException):
        Map(1, 0)

    with pytest.raises(InvalidWorldSizeException):
        Map(-1, 1)

    with pytest.raises(InvalidWorldSizeException):
        Map(1, -1)


def test_place_object():
    game_map = Map(3, 5)
    position = Position(1, 2)
    vacuum = Vacuum()

    # Act
    game_map.place_object(vacuum, position)

    assert game_map.find_object(vacuum.id) == position


def test_place_object_out_of_map_bounds():
    game_map = Map(3, 5)
    vacuum = Vacuum()

    # Act
    with pytest.raises(OutOfMapException):
        game_map.place_object(vacuum, Position(3, 1))

    with pytest.raises(OutOfMapException):
        game_map.place_object(vacuum, Position(1, 5))

    with pytest.raises(OutOfMapException):
        game_map.place_object(vacuum, Position(-1, 1))

    with pytest.raises(OutOfMapException):
        game_map.place_object(vacuum, Position(1, -1))


def test_remove_object():
    game_map = Map(3, 5)
    position = Position(1, 1)
    vacuum = Vacuum()
    game_map.place_object(vacuum, position)

    # Act
    game_map.remove_object(vacuum.id)

    assert game_map.find_object(vacuum.id) is None


def test_increment_position():
    position = Position(3, 2)

    # Act
    position = position.increment(-1, 3)

    # Assert
    assert position.x == 2
    assert position.y == 5


def test_calculate_distance():
    position = Position(4, 1)
    other_position = Position(7, 5)

    # Act
    distance = position.calculate_distance(other_position)

    # Assert
    assert distance == 5
