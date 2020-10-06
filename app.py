from KMapSolver import *


class Solver:
    def __init__(self, map_data, size):
        self.map_data = map_data
        self.all_vars = None
        self.KMapSolver = None
        self.size = int(size)

    def valueToInt(self, current_value):
        values = ['0', '1', 'X']
        return values.index(current_value)

    def setMapData(self):
        if self.size == 2:
            self.map_data = [[
                self.valueToInt(self.map_data[0][0]),
                self.valueToInt(self.map_data[0][1])
            ],
                             [
                                 self.valueToInt(self.map_data[1][0]),
                                 self.valueToInt(self.map_data[1][1])
                             ]]
        if self.size == 3:
            self.map_data = [[
                self.valueToInt(self.map_data[0][0]),
                self.valueToInt(self.map_data[0][1]),
                self.valueToInt(self.map_data[0][2]),
                self.valueToInt(self.map_data[0][3])
            ],
                             [
                                 self.valueToInt(self.map_data[1][0]),
                                 self.valueToInt(self.map_data[1][1]),
                                 self.valueToInt(self.map_data[1][2]),
                                 self.valueToInt(self.map_data[1][3])
                             ]]
        if self.size == 4:
            self.map_data = [[
                self.valueToInt(self.map_data[0][0]),
                self.valueToInt(self.map_data[0][1]),
                self.valueToInt(self.map_data[0][2]),
                self.valueToInt(self.map_data[0][3])
            ],
                             [
                                 self.valueToInt(self.map_data[1][0]),
                                 self.valueToInt(self.map_data[1][1]),
                                 self.valueToInt(self.map_data[1][2]),
                                 self.valueToInt(self.map_data[1][3])
                             ],
                             [
                                 self.valueToInt(self.map_data[2][0]),
                                 self.valueToInt(self.map_data[2][1]),
                                 self.valueToInt(self.map_data[2][2]),
                                 self.valueToInt(self.map_data[2][3])
                             ],
                             [
                                 self.valueToInt(self.map_data[3][0]),
                                 self.valueToInt(self.map_data[3][1]),
                                 self.valueToInt(self.map_data[3][2]),
                                 self.valueToInt(self.map_data[3][3])
                             ]]

    def solveKMap2(self):
        self.all_vars = 'A, B'
        self.KMapSolver = KMapSolver2

    def solveKMap3(self):
        self.all_vars = 'A, B, C'
        self.KMapSolver = KMapSolver3

    def solveKMap4(self):
        self.all_vars = 'A, B, C, D'
        self.KMapSolver = KMapSolver4

    def calc_result(self):
        self.setMapData()
        if self.size == 2:
            self.solveKMap2()
        if self.size == 3:
            self.solveKMap3()
        if self.size == 2:
            self.solveKMap4()
        k = self.KMapSolver(self.map_data)
        k.solve()
        res = k.get_result()
        return res
