import unittest
from drawning import Draw


class TestDrawMethods(unittest.TestCase):

    def setUp(self):
        self.commands = ['C 20 4', 'L 1 2 6 2', 'L 6 3 6 4', 'R 16 1 20 3', 'B 10 3 o', 'Q']
        self.draw = Draw()
        for command in self.commands:
            self.draw.canvas_control(command)

    def test_new_canvas(self):
        self.assertEqual(len(self.draw.canvas[0]), 20)
        self.assertEqual(len(self.draw.canvas), 4)

    def test_draw_line(self):
        for i in range(1 - 1, 6):  # range(x1 - 1, x2)
            self.assertEqual(self.draw.canvas[2 - 1][i], 'x')  # [y2 - 1]
        for j in range(2 - 1, 2):  # range(y1 - 1, y2)
            self.assertEqual(self.draw.canvas[j][1 - 1], 'x')  # [x1 - 1]

    def test_floodFill(self):
        cola = set()
        cola.add((10, 3))

        while len(cola) != 0:
            (x, y) = cola.pop()
            if not self.draw.canvas[y][x] == 'o':
                continue

            self.assertEqual(self.draw.canvas[y][x], 'o')
            self.draw.canvas[y][x] = ' '

            if x > 0:
                cola.add((x-1, y))
            if x < len(self.draw.canvas[y]) - 1:
                cola.add((x+1, y))
            if y > 0:
                cola.add((x, y-1))
            if y < len(self.draw.canvas) - 1:
                cola.add((x, y+1))
