from Classes.TOPSIS import TOPSIS
from Classes.WPM import WPM
from Classes.WSM import WSM

my_matrix = [["weightage", 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2],
          ["names", "Функциональная пригодность", "Уровень производительности", "Совместимость", "Удобство",
           "Удобство использования", "Надёжность", "Защищённость", "Сопровождаемость", "Переносимость", "*Стоимость"],
          ["Экранная камера", 250, 16, 12, 5, 5, 6, 7, 8, 9, 1],
          ["OBS Studio", 200, 16, 8, 3, 2, 3, 5, 6, 7, 2],
          ["UVScreenCamera", 300, 32, 16, 4, 2, 10, 5, 12, 9, 3],
          ["Bandicam", 275, 32, 8, 4, 10, 2, 5, 6, 1, 4],
          ["AVS Video Editor", 225, 16, 16, 2, 1, 6, 3, 7, 2, 5]]
#new comment

if __name__ == '__main__':
    print("TOPSIS")
    method1 = TOPSIS(my_matrix)
    method1.find_best_choice()
    print("----------------------------")
    print("WPM")
    method2 = WPM(my_matrix)
    method2.find_best_option()
    print("----------------------------")
    print("WSM")
    method3 = WSM(my_matrix)
    method3.find_best_option()
    method3.print_matrix()

