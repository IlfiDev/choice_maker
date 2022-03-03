import math


matrix = [["weightage", 0.25, 0.25, 0.25, 0.25],
          ["names", "name1", "name2", "name3", "name4", "name5"],
          ["price", 250, 200, 300, 275, 225],
          ["storage", 16, 16, 32, 32, 16],
          ["Camera", 12, 8, 16, 8, 16],
          ["Looks", 5, 3, 4, 4, 2]]


class TOPSIS:


    def __init__(self, matrix):
        self.matrix = matrix
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
        div = 0
        for i in range(2, len(self.matrix)):
            denominator = math.sqrt(sum(pow(c, 2) for c in self.matrix[i] if type(c) is not str))
            for j in range(1, len(self.matrix[1])):
                self.matrix[i][j] = self.matrix[i][j]/denominator

    def print_matrix(self):
        for cell in self.matrix[0]:
            print(cell, end=" ")
        print()
        for i in range(0, len(self.matrix[1])):
            for j in range(1, len(self.matrix)):
                print(self.matrix[j][i], end=" ")
            print()
        print("V-", end=" ")
        for item in self.v_minus:
            print(item, end=" ")
        print()
        print("V+", end=" ")
        for item in self.v_plus:
            print(item, end=" ")
        print()

    def find_ideal_best_worst(self):
        for i in range(2, len(self.matrix)):
            self.v_plus.append(max(self.matrix[i][1:len(self.matrix[1])]))
            self.v_minus.append(min(self.matrix[i][1:len(self.matrix[1])]))

    def find_distance_to_ideal(self):
        summa1 = 0
        summa2 = 0
        for i in range(1, len(self.matrix[1])):
            for j in range(2, len(self.matrix)):
                summa1 += pow(self.matrix[j][i] - self.v_plus[j - 2], 2)
                summa2 += pow(self.matrix[j][i] - self.v_minus[j - 2], 2)

            self.s_plus.append(math.sqrt(summa1))
            self.s_minus.append(math.sqrt(summa2))
            summa1 = 0
            summa2 = 0

        print(self.s_plus)
        print(self.s_minus)

    def get_performance_score(self):
        for i in range(len(self.s_plus)):
            self.performance_score.append(self.s_minus[i]/(self.s_plus[i] + self.s_minus[i]))

        performance_score_copy = self.performance_score
        for i in range(len(performance_score_copy)):
            max_elem = max(performance_score_copy)
            max_index = performance_score_copy.index(max_elem)
            print(str(self.matrix[1][max_index + 1]) + " - " + str(max_elem))
            performance_score_copy[max_index] = -1

    def weights_mux(self):
        for i in range(2, len(self.matrix)):
            for j in range(1, len(self.matrix[2])):
                self.matrix[i][j] = self.matrix[i][j] * self.matrix[0][i - 1]


if __name__ == '__main__':
    phones = TOPSIS(matrix)
    phones.find_best_choice()

