import copy
import math
from tabulate import tabulate


class TOPSIS:

    def __init__(self, matrix):
        self.matrix = copy.deepcopy(matrix)
        self.v_plus = []
        self.v_minus = []
        self.s_plus = []
        self.s_minus = []
        self.performance_score = []

    def find_best_choice(self):
        self.normalize_matrix()
        self.weights_mux()
        self.find_ideal_best_worst()
        self.print_matrix()
        self.find_distance_to_ideal()
        self.get_performance_score()

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

    def weights_mux(self):
        for j in range(1, len(self.matrix[0])):
            for i in range(2, len(self.matrix)):
                self.matrix[i][j] = self.matrix[i][j] * self.matrix[0][j]

    def find_ideal_best_worst(self):
        for j in range(1, len(self.matrix[0])):
            row = [self.matrix[c][j] for c in range(2, len(self.matrix))]
            self.v_plus.append(max(row))
            self.v_minus.append(min(row))

    def find_distance_to_ideal(self):
        for i in range(2, len(self.matrix)):
            self.s_plus.append(math.sqrt(sum([pow(
                self.matrix[i][c] - self.v_plus[c - 1], 2) for c in range(
                    1, len(self.matrix[0]))])))
            self.s_minus.append(math.sqrt(sum([pow(
                self.matrix[i][c] - self.v_minus[c - 1], 2) for c in range(
                    1, len(self.matrix[0]))])))

    def get_performance_score(self):
        for i in range(len(self.s_plus)):
            self.performance_score.append(self.s_minus[i]/(self.s_plus[i] + self.s_minus[i]))
        performance_score_copy = self.performance_score
        counter = 1
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
