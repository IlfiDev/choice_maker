import copy
import math

from tabulate import tabulate

class WPM:
    def __init__(self, matrix):
        self.matrix = copy.deepcopy(matrix)
        self.wpm_performance_score = []

    def find_best_option(self):
        self.normalize_matrix()
        self.calculate_wpm_performance_score()
        self.get_performance_score()

    def normalize_matrix2(self):
        for j in range(1, len(self.matrix[0])):
            row = [self.matrix[c][j] for c in range(2, len(self.matrix))]
            for i in range(2, len(self.matrix)):
                if "*" in self.matrix[1][j]:
                    if self.matrix[i][j] == 0:
                        self.matrix = min(row)
                    else:
                        self.matrix[i][j] = min(row) / self.matrix[i][j]
                else:
                    self.matrix[i][j] = self.matrix[i][j] / max(row)

    def normalize_matrix(self):
        for j in range(1, len(self.matrix[0])):
            sum_of_pow = 0
            for i in range(2, len(self.matrix)):
                sum_of_pow += pow(self.matrix[i][j], 2)
            denominator = math.sqrt(sum_of_pow)
            for i in range(2, len(self.matrix)):
                if "*" in self.matrix[1][j]:
                    self.matrix[i][j] = 1 - self.matrix[i][j]/denominator
                else:
                    self.matrix[i][j] = self.matrix[i][j]/denominator

    def calculate_wpm_performance_score(self):
        wpm = copy.deepcopy(self.matrix)
        for j in range(1, len(wpm[0])):
            for i in range(2, len(wpm)):
                wpm[i][j] = pow(wpm[i][j], wpm[0][j])
        for i in range(2, len(wpm)):
            product = 1
            for j in range(1, len(wpm[0])):
                if wpm[i][j] == 0:
                    product *= 1
                else:
                    product *= wpm[i][j]
            self.wpm_performance_score.append(product)

    def get_performance_score(self):
        counter = 1
        performance_score_copy = self.wpm_performance_score.copy()
        for i in range(len(performance_score_copy)):
            max_elem = max(performance_score_copy)
            max_index = performance_score_copy.index(max_elem)
            print(str(counter) + " - " + str(self.matrix[max_index + 2][0]) + " - " + str(max_elem))
            performance_score_copy[max_index] = -1
            counter += 1

    def print_matrix(self):
        print(tabulate(
            [j for j in [
                i for i in
                self.matrix[1:len(self.matrix)]]], headers=self.matrix[0]))