class Brick:

    def __init__(self, parts, color):
        self._parts = parts
        self._color = color

    @property
    def parts(self):
        return self._parts

    @property
    def color(self):
        return self._color

