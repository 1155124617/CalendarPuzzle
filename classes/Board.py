import numpy as np

from classes.Cell import Cell

class Board:

    def __init__(self):
        self._rows = 8
        self._cols = 7
        self._cells = [[Cell("Jan"), Cell("Feb"), Cell("Mar"), Cell("Apr"), Cell("May"),  Cell("June"), None],
                       [Cell("Jul"), Cell("Aug"), Cell("Sep"), Cell("Oct"), Cell("Nov"),  Cell("Dec"),  None],
                       [Cell('1'),   Cell('2'),   Cell('3'),   Cell('4'),   Cell('5'),    Cell('6'),    Cell('7')],
                       [Cell('8'),   Cell('9'),   Cell('10'),  Cell('11'),  Cell('12'),   Cell('13'),   Cell('14')],
                       [Cell('15'),  Cell('16'),  Cell('17'),  Cell('18'),  Cell('19'),   Cell('20'),   Cell('21')],
                       [Cell('22'),  Cell('23'),  Cell('24'),  Cell('25'),  Cell('26'),   Cell('27'),   Cell('28')],
                       [Cell('29'),  Cell('30'),  Cell('31'),  Cell("Sun"), Cell("Mon"),  Cell("Tues"), Cell("Wed")],
                       [None,        None,        None,        None,        Cell("Thur"), Cell("Fri"),  Cell("Sat")]]

    @property
    def rows(self):
        return self._rows

    @property
    def cols(self):
        return self._cols

    def set_day(self, month, day, day_of_the_week):
        for i in range(self._rows):
            for j in range(self._cols):
                if self._cells[i][j] is not None:
                    if self._cells[i][j].content == month:
                        self._cells[i][j].occupy("special")
                    if self._cells[i][j].content == day:
                        self._cells[i][j].occupy("special")
                    if self._cells[i][j].content == day_of_the_week:
                        self._cells[i][j].occupy("special")

    def put_brick(self, x, y, brick):
        for part in brick.parts:
            if (x+part[0]) not in range(self._rows) or (y+part[1]) not in range(self._cols):
                return False
            cell = self._cells[x+part[0]][y+part[1]]
            if cell is None or cell.is_occupied():
                return False

        for part in brick.parts:
            self._cells[x+part[0]][y+part[1]].occupy(brick)
        return True

    def remove_brick(self, x, y, brick):
        for part in brick.parts:
            self._cells[x+part[0]][y+part[1]].remove_occupant()

    def transform_to_array(self):
        """
        Return type is numpy.array
        """
        array = np.zeros((self._rows, self._cols))
        for i in range(self._rows):
            for j in range(self._cols):
                array[i, j] = 1 if self._cells[i][j] is None or self._cells[i][j].is_occupied() else 0
        return array

    def display(self):
        for row in self._cells:
            for cell in row:
                if cell is None:
                    print("        ", end='')
                else:
                    cell.display()
            print()
        print()
