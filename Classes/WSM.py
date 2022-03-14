import copy
from tabulate import tabulate

class WSM:
    def __init__(self, matrix):
        self.matrix = copy.deepcopy(matrix)
        self.wsm_performance_score = []

    def find_best_option(self):
        self.normalize_matrix()
        self.calculate_performance_score()
        self.get_performance_score()


    def normalize_matrix(self):
        for j in range(1, len(self.matrix[0])):
            row = [self.matrix[c][j] for c in range(2, len(self.matrix))]
            for i in range(2, len(self.matrix)):
                if "*" in self.matrix[1][j]:
                    self.matrix[i][j] = min(row) / self.matrix[i][j]
                else:
                    self.matrix[i][j] = self.matrix[i][j] / max(row)

    def calculate_performance_score(self):
        wsm = copy.deepcopy(self.matrix)
        for j in range(1, len(wsm[0])):
            for i in range(2, len(wsm)):
                wsm[i][j] = wsm[i][j] * wsm[0][j]
        for i in range(2, len(wsm)):
            self.wsm_performance_score.append(sum(wsm[i][1:len(wsm[0])]))

    def get_performance_score(self):
        counter = 1
        performance_score_copy = self.wsm_performance_score.copy()
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
