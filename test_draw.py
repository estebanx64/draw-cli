import unittest
from draw import Main


class TestDrawMethods(unittest.TestCase):

    def setUp(self):
        self.matriz = [20, 4]
        self.line1 = [1, 2, 6, 2]
        self.line2 = [6, 3, 6, 4]
        self.rectangle = [16, 1, 20, 3]
        self.fill = [10, 3, 'o']

        self.obj = Main()
        self.obj.newMatriz(*self.matriz)
        self.obj.line(*self.line1)
        self.obj.line(*self.line2)
        self.obj.rectangle(*self.rectangle)
        self.obj.floodFill(*self.fill)

    def test_newMatriz(self):
        self.assertEqual(len(self.obj.matriz[0]), self.matriz[0])
        self.assertEqual(len(self.obj.matriz), self.matriz[1])

    def test_line(self):
        for i in range(self.line1[0] - 1, self.line1[2]):
            self.assertEqual(self.obj.matriz[self.line1[3] - 1][i], 'x')
        for j in range(self.line2[1] - 1, self.line2[3]):
            self.assertEqual(self.obj.matriz[j][self.line2[0] - 1], 'x')

    def test_rectangle(self):
        for i in range(self.rectangle[0] - 1, self.rectangle[2]):
            self.assertEqual(self.obj.matriz[self.rectangle[1] - 1][i], 'x')
            self.assertEqual(self.obj.matriz[self.rectangle[3] - 1][i], 'x')
        for j in range(self.rectangle[1] - 1, self.rectangle[3]):
            self.assertEqual(self.obj.matriz[j][self.rectangle[0] - 1], 'x')
            self.assertEqual(self.obj.matriz[j][self.rectangle[2] - 1], 'x')

    def test_floodFill(self):
        cola = set()
        cola.add((self.fill[0], self.fill[1]))

        while len(cola) != 0:
            (x, y) = cola.pop()
            if not self.obj.matriz[y][x] == 'o':
                continue

            self.assertEqual(self.obj.matriz[y][x], self.fill[2])
            self.obj.matriz[y][x] = ' '

            if x > 0:
                cola.add((x-1, y))
            if x < len(self.obj.matriz[y]) - 1:
                cola.add((x+1, y))
            if y > 0:
                cola.add((x, y-1))
            if y < len(self.obj.matriz) - 1:
                cola.add((x, y+1))


if __name__ == '__main__':
    unittest.main()
