import pyray

class Color:

    WHITE = (255, 255, 255, 255)
    RED = (255, 0, 0, 255)
    BLACK = (0, 0, 0, 255)
    YELLOW = (255, 255, 0, 255)

    def __init__(self, r, g, b, a):
        self.r = r
        self.g = g
        self.b = b
        self.a = a