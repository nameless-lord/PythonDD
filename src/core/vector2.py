import pyray

class Vector2:
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y


    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)


    def to_rl_vector(self) -> pyray.Vector2:
        return pyray.Vector2(self.x, self.y)