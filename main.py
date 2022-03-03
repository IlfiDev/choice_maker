from Classes.TOPSIS import TOPSIS

matrix = [["weightage", 0.25, 0.25, 0.25, 0.25],
          ["names", "name1", "name2", "name3", "name4", "name5"],
          ["price", 250, 200, 300, 275, 225],
          ["storage", 16, 16, 32, 32, 16],
          ["Camera", 12, 8, 16, 8, 16],
          ["Looks", 5, 3, 4, 4, 2]]




if __name__ == '__main__':
    phones = TOPSIS(matrix)
    phones.find_best_choice()

