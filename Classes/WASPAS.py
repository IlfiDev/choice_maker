import copy

from tabulate import tabulate

class WASPAS:

    def __init__(self, matrix, joined_generalized_criteria):
        self.matrix = matrix
        self.wsm_performance_score = []
        self.wpm_performance_score = []
        self.performance_score = []
        self.jgc = joined_generalized_criteria

    def find_best_option(self):
        self.normalize_matrix()
        self.calculate_wsm_performance_score()
        self.calculate_wpm_performance_score()
        self.calculate_performance()
        self.get_performance_score()

    def normalize_matrix(self):
        for j in range(1, len(self.matrix[0])):
            row = [self.matrix[c][j] for c in range(2, len(self.matrix))]
            for i in range(2, len(self.matrix)):
                if "*" in self.matrix[1][j]:
                    self.matrix[i][j] = min(row) / self.matrix[i][j]
                else:
                    self.matrix[i][j] = self.matrix[i][j] / max(row)

    def calculate_wsm_performance_score(self):

        wsm = copy.deepcopy(self.matrix)
        for j in range(1, len(wsm[0])):
            for i in range(2, len(wsm)):
                wsm[i][j] = wsm[i][j] * wsm[0][j]
        for i in range(2, len(wsm)):
            self.wsm_performance_score.append(sum(wsm[i][1:len(wsm[0])]))

    def calculate_wpm_performance_score(self):
        wpm = copy.deepcopy(self.matrix)
        for j in range(1, len(wpm[0])):
            for i in range(2, len(wpm)):
                wpm[i][j] = pow(wpm[i][j], wpm[0][j])
        for i in range(2, len(wpm)):
            product = 1
            for j in range(1, len(wpm[0])):
                product *= wpm[i][j]
            self.wpm_performance_score.append(product)

    def calculate_performance(self):
        for i in range(len(self.wpm_performance_score)):
            self.performance_score.append(
                self.jgc * self.wsm_performance_score[i] + (1 - self.jgc) * self.wpm_performance_score[i])

    def get_performance_score(self):
        counter = 1
        performance_score_copy = self.performance_score.copy()
        for i in range(len(performance_score_copy)):
            max_elem = max(performance_score_copy)
            max_index = performance_score_copy.index(max_elem)
            print(str(counter) + " - " + str(self.matrix[max_index + 2][0]) + " - " + str(max_elem))
            performance_score_copy[max_index] = -1
            counter += 1
