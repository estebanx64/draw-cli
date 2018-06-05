import os


class Main:

    matriz = []

    def printMatriz(self):
        cadena = ""
        for x in range(len(self.matriz)):
            for y in range(len(self.matriz[x])):
                cadena += str(self.matriz[x][y])
            print('|' + cadena + '|')
            cadena = ""

    def newMatriz(self, x, y):
        self.matriz = [[' ' for x in range(x)] for y in range(y)]
        # return matriz

    def line(self, x1, y1, x2, y2):
        if y1 == y2:
            for x in range(x1 - 1, x2):
                self.matriz[y2 - 1][x] = 'x'
        elif x1 == x2:
            for y in range(y1 - 1, y2):
                self.matriz[y][x1 - 1] = 'x'

    def rectangle(self, x1, y1, x2, y2):
        for x in range(x1 - 1, x2):
            self.matriz[y1 - 1][x] = 'x'
            self.matriz[y2 - 1][x] = 'x'
        for y in range(y1 - 1, y2):
            self.matriz[y][x1 - 1] = 'x'
            self.matriz[y][x2 - 1] = 'x'

    def floodFill(self, x, y, replacement):
        fill = set()
        fill.add((x, y))

        while len(fill) != 0:
            (x, y) = fill.pop()
            if not self.matriz[y][x] == ' ':
                continue
            self.matriz[y][x] = replacement
            # print(x, y)
            if x > 0:
                fill.add((x-1, y))
            if x < len(self.matriz[y]) - 1:
                fill.add((x+1, y))
            if y > 0:
                fill.add((x, y-1))
            if y < len(self.matriz) - 1:
                fill.add((x, y+1))

    def run(self):
        command = input('Enter command: ').split(" ")
        while not command[0].upper() == 'Q':
            try:
                if command[0].upper() == 'C':
                    x = int(command[1])
                    y = int(command[2])
                    self.newMatriz(x, y)
                    self.printMatriz()

                elif command[0].upper() == 'L':
                    x1 = int(command[1])
                    y1 = int(command[2])
                    x2 = int(command[3])
                    y2 = int(command[4])

                    self.line(x1, y1, x2, y2)
                    os.system("clear")
                    self.printMatriz()

                elif command[0].upper() == 'R':
                    x1 = int(command[1])
                    y1 = int(command[2])
                    x2 = int(command[3])
                    y2 = int(command[4])

                    self.rectangle(x1, y1, x2, y2)
                    os.system("clear")
                    self.printMatriz()

                elif command[0].upper() == 'B':
                    x = int(command[1])
                    y = int(command[2])
                    self.floodFill(x - 1, y - 1, command[3])
                    os.system("clear")
                    self.printMatriz()

                else:
                    print('El comando no es valido')

                command = input('Enter command: ').split(" ")
            except Exception:
                print('El comando no es valido')
                command = input('Enter command: ').split(" ")


if __name__ == '__main__':
    obj = Main()
    obj.run()
