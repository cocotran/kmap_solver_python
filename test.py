from KMapSolver import *


class Solver:
    def __init__(self, parent=None):
        self.map_data = None
        self.all_vars = None
        self.KMapSolver = None

    def valueToInt(self, current_value):
        values = ['0', '1', 'X']
        return values.index(current_value)

    def solveKMap2(self):
        self.map_data = [[self.valueToInt('1'),
                          self.valueToInt('X')],
                         [self.valueToInt('0'),
                          self.valueToInt('1')]]
        self.all_vars = 'A, B'
        self.KMapSolver = KMapSolver2
        # self.result2VarsEditText.setText("F({0}) = {1}".format(
        #     self.all_vars, self.calc_result(2)))

    def solveKMap3(self):
        self.map_data = [[
            self.valueToInt(self.but_3__0_0.text()),
            self.valueToInt(self.but_3__0_1.text()),
            self.valueToInt(self.but_3__0_2.text()),
            self.valueToInt(self.but_3__0_3.text())
        ],
                         [
                             self.valueToInt(self.but_3__1_0.text()),
                             self.valueToInt(self.but_3__1_1.text()),
                             self.valueToInt(self.but_3__1_2.text()),
                             self.valueToInt(self.but_3__1_3.text())
                         ]]

        self.all_vars = 'A, B, C'
        self.KMapSolver = KMapSolver3
        # self.result3VarsEditText.setText("F({0}) = {1}".format(
        #     self.all_vars, self.calc_result(3)))

    def solveKMap4(self):
        self.map_data = [[
            self.valueToInt(self.but_4__0_0.text()),
            self.valueToInt(self.but_4__0_1.text()),
            self.valueToInt(self.but_4__0_2.text()),
            self.valueToInt(self.but_4__0_3.text())
        ],
                         [
                             self.valueToInt(self.but_4__1_0.text()),
                             self.valueToInt(self.but_4__1_1.text()),
                             self.valueToInt(self.but_4__1_2.text()),
                             self.valueToInt(self.but_4__1_3.text())
                         ],
                         [
                             self.valueToInt(self.but_4__2_0.text()),
                             self.valueToInt(self.but_4__2_1.text()),
                             self.valueToInt(self.but_4__2_2.text()),
                             self.valueToInt(self.but_4__2_3.text())
                         ],
                         [
                             self.valueToInt(self.but_4__3_0.text()),
                             self.valueToInt(self.but_4__3_1.text()),
                             self.valueToInt(self.but_4__3_2.text()),
                             self.valueToInt(self.but_4__3_3.text())
                         ]]
        self.all_vars = 'A, B, C, D'
        self.KMapSolver = KMapSolver4
        self.result4VarsEditText.setText("F({0}) = {1}".format(
            self.all_vars, self.calc_result(4)))

    def calc_result(self):
        k = self.KMapSolver(self.map_data)
        k.solve()
        res = k.get_result()
        return res


kmap = Solver()
kmap.solveKMap2()
# print(kmap.calc_result())
print(kmap.map_data)