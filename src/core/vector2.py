import pyray

class Vector2:
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y


    def to_rl_vector(self) -> pyray.Vector2:
        return pyray.Vector2(self.x, self.y)