class Chunk:
    def __init__(self, coords, size=100):
        self.size = size
        self.chunk = [[0 for x in range(size)] for y in range(size)]
        self.sum = 0
        self.coords = coords

    def increment_case(self, x, y):
        if 0 <= x < 100 and 0 <= y < 100:
            self.chunk[x][y] += 1
            self.sum += 1

    def get_average(self):
        return self.sum / (self.size * self.size)

    def __str__(self):
        string = str(self.coords) + '\n'
        for i in range(self.size):
            string += str(self.chunk[i]) + '\n'

        return string
