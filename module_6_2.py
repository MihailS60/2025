class Vehicle:
    # # Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    __COLOR_VARIANTS=['blue', 'red', 'green', 'black', 'white']

    change_color_flag=True                        # флаг измений цвета
    change_owner_flag = True                      # флаг измений владельца

    def __init__(self, owner,model,color,engine_power):
        self.owner=owner
        self.__model=model
        self.__engine_power=engine_power
        self.__color=color

    def get_model(self):                      # "Модель: <название модели транспорта>"
        return self.__model


    def get_horsepower(self):                 # "Мощность двигателя: <мощность>"
        return self.__engine_power


    def get_color(self):                      # "Цвет: <цвет транспорта>"
        return self.__color


    def print_info(self):                       # результаты методов
        print(f"Модель: {self.__model}")
        print(f"Мощность двигателя: {self.__engine_power}")
        if self.change_color_flag:
            print(f"Цвет: {self.__color}")
        else:
            print("Цвет:","\033[32m",f"{self.__color}","\033[0m")
        if self.change_owner_flag:
            print(f"Владелец: {self.owner}")
        else:
            print("Владелец:","\033[32m",f"{self.owner}","\033[0m")


    def set_color(self,new_color):

        # Проверка в __COLOR_VARIANTS происходит не учитывая регистр
        if new_color.lower() in Vehicle.__COLOR_VARIANTS:
            self.__color=new_color

            Vehicle.change_color_flag=False           # произведены изменения цвета
        else:
            print("\033[31m",f"Нельзя сменить цвет на {new_color}","\033[0m")


class Myclass:  # разделитель
        @staticmethod
        def staticmethod():
            print("\033[33m", "_" * 20, "\033[0m")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


print("\033[34m","Задача 'Изменять нельзя получать':","\033[0m","\n","\033[33m","_" * 20,"\033[0m")

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle1.print_info()                         # Изначальные свойства

Myclass.staticmethod()               # разделитель

# Меняем свойства (в т.ч. вызывая методы)

vehicle1.set_color('PINK')
vehicle1.set_color('BLACK')

vehicle1.owner = 'Vasyok'
vehicle1.change_owner_flag=False           # произведены изменения владельца

Myclass.staticmethod()                   # разделитель
# Проверяем что поменялось
vehicle1.print_info()
Myclass.staticmethod()                   # разделитель
