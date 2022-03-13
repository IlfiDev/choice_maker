from Classes.TOPSIS import TOPSIS
from Classes.WASPAS import WASPAS

my_matrix = [["weightage", 0.25, 0.25, 0.25, 0.25],
          ["names", "*price", "storage", "Camera", "Look"],
          ["phone 1", 250, 16, 12, 5],
          ["phone 2", 200, 16, 8, 3],
          ["phone 3", 300, 32, 16, 4],
          ["phone 4", 275, 32, 8, 4],
          ["phone 5", 225, 16, 16, 2]]
#new comment

if __name__ == '__main__':
    phones = TOPSIS(my_matrix)
    phones.find_best_choice()
    phones = WASPAS(my_matrix, 0.5)
    phones.find_best_option()

