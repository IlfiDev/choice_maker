from Classes.TOPSIS import TOPSIS

matrix = [["weightage", 0.25, 0.25, 0.25, 0.25],
          ["names", "*price", "storage", "Camera", "Look"],
          ["phone 1", 250, 16, 12, 5],
          ["phone 2", 200, 16, 8, 3],
          ["phone 3", 300, 32, 16, 4],
          ["phone 4", 275, 32, 8, 4],
          ["phone 5", 225, 16, 16, 2]]


if __name__ == '__main__':
    phones = TOPSIS(matrix)
    phones.find_best_choice()

