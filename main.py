from Game import Game
from settings import Settings
from tile import Tile

if __name__ == "__main__":
    pass
    # game = Game()
    # game.on_execute()

settings = Settings()
print(settings.get(((Tile.TILE, "direction", "top", "state", "idle", "position", "row", "hero"), (Tile.TILE, "direction", "top", "state", "idle", "position", "col", "hero"))))
