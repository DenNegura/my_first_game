from SingletonMeta import SingletonMeta


class ContextID:
    TILE = "tile"

    SPRITE = "sprite"

    MAP_SIZE = "map_size"


class Context(metaclass=SingletonMeta):
    _instance = None

    def __init__(self):
        self._container = {}
        self._subscribers = {}

    def set(self, obj, obj_id: str):
        self._container[obj_id] = obj

    def send(self, obj, obj_id: str):
        subscribers = self._subscribers.get(obj_id)
        if subscribers:
            for subscriber in subscribers:
                subscriber(obj)

    def get(self, obj_id):
        return self._container.get(obj_id)

    def subscribe(self, callback, obj_id: str):
        subscribers = self._subscribers.get(obj_id)
        if subscribers:
            subscribers.append(callback)
        else:
            self._subscribers[obj_id] = [callback]
        return

    def remove(self, obj_id):
        return self._container.pop(obj_id, None)

    def unsubscribe(self, callback, obj_id: str):
        subscribers = self._subscribers.get(obj_id)
        if subscribers:
            subscribers.remove(callback)
