import os

from game_builder import GameBuilder

if __name__ == "__main__":
    # game = Game()
    # game.on_execute()
    directory = os.path.dirname(os.path.abspath(__file__))
    print(directory)
    print("Current working directory:", os.getcwd())
    builder = GameBuilder()
    builder.mainloop()
