class HexColor:
    def __init__(self):
        self.colors = {
            'red'   :   '#ff0000',
            'greed' :   '#7cfc00',
            'blue'  :   '#4169e1'
        }
 
hex_color = HexColor()
print(hex_color.colors['red'])   # Получим: #ff0000
 
 
# Пример 2: Удваиваем число
class DoubleMe:
    def __init__(self, number):
        self.result = number * 2
 
Double = DoubleMe(2)
print(Double.result)             # Получим 4


class Class1:
    def __init__(self): # Конструктор класса
        print("Вызван метод __init__()")
    def __del__(self):  # Деструктор класса
        print ("Вызван метод __del__()")
c1 = Class1()          # Выведет: Вызван метод __init__()
del c1                 # Выведет: Вызван метод __del__()
c2 = Class1()          # Выведет: Вызван метод __init__()
c3 = c2                # Создаем ссылку на экземпляр класса
del c2                 # Ничего не выведет
del c3                 # Выведет: Вызван метод __del__() 