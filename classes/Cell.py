class Cell:

    def __init__(self, content):
        self._occupant = None
        self._content = content

    def occupy(self, occupant):
        self._occupant = occupant

    @property
    def content(self):
        return self._content

    def is_occupied(self):
        return self._occupant is not None

    def remove_occupant(self):
        self._occupant = None

    def display(self):
        content = None
        if len(self._content) == 1:
            content = "   {}  ".format(self._content)
        elif len(self._content) == 2:
            content = "  {}  ".format(self._content)
        elif len(self._content) == 3:
            content = "  {} ".format(self._content)
        elif len(self._content) == 4:
            content = " {} ".format(self._content)
        if self._occupant is None or self._occupant == "special":
            print("{}  ".format(content), end='')
        else:
            print("{}{}\033[0m  ".format(self._occupant.color, content), end='')
