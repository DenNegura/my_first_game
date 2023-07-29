class State:
    def __init__(self, state: str):
        self._state = state

    def get(self):
        return self._state


IDLE = State("idle")

WALK = State("walk")

RUN = State("run")

STATES = [IDLE, WALK, RUN]