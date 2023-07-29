class Direction:
    def __init__(self, direction: str, change):
        self._direction = direction
        self._change = change

    def get(self):
        return self._direction

    def change(self, x: int, y: int, speed: int):
        return self._change(x, y, speed)


TOP = Direction("top", lambda x, y, spd: (x, y - spd))

RIGHT = Direction("right", lambda x, y, spd: (x + spd, y))

BOTTOM = Direction("bottom", lambda x, y, spd: (x, y + spd))

LEFT = Direction("left", lambda x, y, spd: (x - spd, y))

TOP_RIGHT = Direction("top_right", lambda x, y, spd: (x + spd, y - spd))

TOP_LEFT = Direction("top_left", lambda x, y, spd: (x - spd, y - spd))

BOTTOM_RIGHT = Direction("bottom_right", lambda x, y, spd: (x + spd, y + spd))

BOTTOM_LEFT = Direction("bottom_left", lambda x, y, spd: (x - spd, y + spd))

DIRECTIONS = [TOP, RIGHT, LEFT, BOTTOM, TOP_RIGHT, TOP_LEFT, BOTTOM_RIGHT, BOTTOM_LEFT]