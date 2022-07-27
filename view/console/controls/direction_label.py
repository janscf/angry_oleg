from lib.game.enums import Direction


class DirectionLabel:
    DIRECTION_TEXT = {
        Direction.North: 'север',
        Direction.South: 'юг',
        Direction.West: 'запад',
        Direction.East: 'восток',
        Direction.NorthWest: 'северо-запад',
        Direction.NorthEast: 'северо-восток',
        Direction.SouthWest: 'юго-запад',
        Direction.SouthEast: 'юго-восток',
    }

    def __init__(self, direction: 'Direction'):
        self.__label = self.DIRECTION_TEXT[direction]

    def __str__(self) -> str:
        return self.__label
