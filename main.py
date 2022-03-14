from Classes.TOPSIS import TOPSIS
from Classes.WPM import WPM
from Classes.WSM import WSM

my_matrix = [["weightage", 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.3],
          ["names", "Функциональная пригодность", "Уровень производительности", "Совместимость",
           "Удобство использования", "Надёжность", "Защищённость", "Сопровождаемость", "Переносимость", "*Стоимость"],
          ["Экранная камера", 1, 4, 1, 3, 2, 3, 2, 1, 665],
          ["OBS Studio", 3, 4, 3, 4, 4, 1, 2, 0, 0],
          ["UVScreenCamera", 2, 4, 2, 2, 2, 3, 1, 1, 990],
          ["Bandicam", 2, 4, 3, 1, 2, 1, 0, 0, 4000],
          ["AVS Video Editor", 1, 2, 3, 3, 3, 3, 2, 1, 2000]]
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

