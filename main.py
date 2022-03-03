# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math




matrix = [["weightage", 0.25, 0.25, 0.25, 0.25],
          ["names", "name1", "name2", "name3", "name4", "name5"],
          ["price", 250, 200, 300, 275, 225],
          ["storage", 16, 16, 32, 32, 16],
          ["Camera", 12, 8, 16, 8, 16],
          ["Looks", 5, 3, 4, 4, 2]]




def TOPSIS(matr):
    normalize_matrix(matr)
    weights_mux(matr)
    find_ideal_best_worst(matr, v_plus, v_minus)
    print_matrix(matr)
    find_distance_to_ideal(matr, s_plus, s_minus)
    get_performance_score()


def normalize_matrix(matrix):
    div = 0
    for i in range(2, len(matrix)):
        denominator = math.sqrt(sum(pow(c, 2) for c in matrix[i] if type(c) is not str))
        for j in range(1, len(matrix[1])):
            matrix[i][j] = matrix[i][j]/denominator


v_plus = []
v_minus = []
s_plus = []
s_minus = []


def print_matrix(matr):
    for cell in matrix[0]:
        print(cell, end=" ")
    print()
    for i in range(0, len(matr[1])):
        for j in range(1, len(matr)):
            print(matrix[j][i], end=" ")
        print()
    print("V-", end=" ")
    for item in v_minus:
        print(item, end=" ")
    print()
    print("V+", end=" ")
    for item in v_plus:
        print(item, end=" ")
    print()


def find_ideal_best_worst(matr, plus, minus):
    for i in range(2, len(matr)):
        plus.append(max(matr[i][1:len(matr[1])]))
        minus.append(min(matr[i][1:len(matr[1])]))


def find_distance_to_ideal(matr, plus, minus):
    summa1 = 0
    summa2 = 0
    for i in range(1, len(matr[1])):
        for j in range(2, len(matr)):

            summa1 += pow(matrix[j][i] - v_plus[j - 2], 2)
            summa2 += pow(matrix[j][i] - v_minus[j - 2], 2)
        plus.append(math.sqrt(summa1))
        minus.append(math.sqrt(summa2))
        summa1 = 0
        summa2 = 0
    print(plus)
    print(minus)


performance_score = []

def get_performance_score():
    for i in range(len(s_plus)):
        performance_score.append(s_minus[i]/(s_plus[i] + s_minus[i]))

    performance_score_copy = performance_score
    for i in range(len(performance_score_copy)):
        max_elem = max(performance_score_copy)
        max_index = performance_score_copy.index(max_elem)
        print(str(matrix[1][max_index + 1]) + " - " + str(max_elem))
        performance_score_copy[max_index] = -1


def weights_mux(matr):
    for i in range(2, len(matr)):
        for j in range(1, len(matr[2])):
            matr[i][j] = matr[i][j] * matr[0][i - 1]



if __name__ == '__main__':
    TOPSIS(matrix)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
