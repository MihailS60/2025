class House:
    def __init__(self,name,number_of_floors):
        self.name=name                              # имя
        self.number_of_floors=number_of_floors      # кол-во этажей


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



#   неправильный выбор этажей :
h1 = House('ЖК Горский', 18)
print(f'объект {h1.name}, этажность {h1.number_of_floors}')
h1.go_to(19)

h2 = House('Домик в деревне', 2)
print(f'объект {h2.name}, этажность {h2.number_of_floors}')
h2.go_to(10)

#   правильный выбор этажей :

h1 = House('ЖК Горский', 18)
print(f'объект {h1.name}, этажность {h1.number_of_floors}')
h1.go_to(15)

h2 = House('Домик в деревне', 2)
print(f'объект {h2.name}, этажность {h2.number_of_floors}')
h2.go_to(2)

# __str__
print(h1,"\n",h2)
print("\033[33m","_" * 20,"\033[0m")

# __len__
print(f'объект {h1.name} метод __len__',len(h1))
print(f'объект {h2.name} метод __len__',len(h2))


print("\033[33m","_" * 20,"\033[0m")
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1,"\n",h2)
print("\033[33m","_" * 20,"\033[0m")

print("метод __eq__  ", h1 == h2)                  # __eq__
print("\033[33m","_" * 20,"\033[0m")

add_floor=10
h1 = h1 + add_floor                              # __add__
print(h1)
print("\033[33m","_" * 20,"\033[0m")
print("метод __eq__  ", h1 == h2)                  # __eq__
print("\033[33m","_" * 20,"\033[0m")

h1 += 10                                          # __iadd__
print(h1)
print("\033[33m","_" * 20,"\033[0m")

h2 = 10 + h2                                      # __radd__
print(h2)
print("\033[33m","_" * 20,"\033[0m")

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__