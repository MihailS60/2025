class House:

    houses_history = []

    def __new__(cls, args, **kwargs):
            House.houses_history.append(args)
            return object.__new__(cls)

    def __init__(self, first, second):
        self.name=first
        self.number_of_floors=second

    def __del__(self):
        print(f" объект {self.name} снесён, но он останется в истории")



    def go_to(self,new_floor):
            if new_floor <= self.number_of_floors:
               print("выбранный этаж : ")
               fl_ = (i for i in range(1, new_floor+1))   # печать этажей
               for i in fl_:
                   print("\033[34m",i,"\033[0m",end=" ")
            else:
                print(f" этажа {new_floor} не существует")

            print("\n","\033[33m","_" * 20,"\033[0m")



    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}  и кол-во этажей:  {self.number_of_floors}'


    def __add__(self, value):
        if not isinstance(value, int):
            print("Правый операнд должен быть типом int")
        else:
            self.number_of_floors +=value
            print("Выполняется метод __add__.")
        return self

    def __iadd__(self, value):
        if not isinstance(value, int):
            print("после равенства единственный операнд должен быть типом int")
        else:
            self.number_of_floors +=value
            print("Выполняется метод __iadd__.")
        return self

    def __radd__(self, value):
        if not isinstance(value, int):
            print("Левый операнд должен быть типом int")
        else:
            self.number_of_floors +=value
            print("Выполняется метод __radd__.")
        return self



    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors==other.number_of_floors
        else:
            print("other не указывает на объект типа House")

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        else:
            print("other не указывает на объект типа House")

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        else:
            print("other не указывает на объект типа House")

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        else:
            print("other не указывает на объект типа House")

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        else:
            print("other не указывает на объект типа House")

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        else:
            print("other не указывает на объект типа House")


    def pr_report(self, name, number_fl):
        print(f'объект {name}, этажность {number_fl}')
        Myclass.staticmethod()  # разделитель
        print("\n", "\033[34m", "Хранилище названий созданных объектов : ", "\033[0m", House.houses_history)
        Myclass.staticmethod()  # разделитель

class Myclass:  # разделитель
    @staticmethod
    def staticmethod():
            print("\033[33m", "_" * 20, "\033[0m")


Myclass.staticmethod()          # разделитель

h1 = House('ЖК Горский', second=10)
h1.pr_report(h1.name,h1.number_of_floors)

h2 = House('ЖК Акация', second=20)
h2.pr_report(h1.name,h2.number_of_floors)

h3 = House('ЖК Матрёшки', second=20)
h3.pr_report(h3.name,h3.number_of_floors)

del h2
del h3

print("\n","\033[34m","Хранилище названий созданных объектов : ","\033[0m", House.houses_history)
