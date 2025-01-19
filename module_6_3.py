import random

class Animal:
    live = True
    sound = None                                    # звук (изначально отсутствует)
    _DEGREE_OF_DANGER = 0                           # степень опасности существа
    _cords = [0,0,0]

    def __init__(self, speed):
        self.speed=speed


    def move(self,dx,dy, dz):
        self._cords[0] = dx
        self._cords[1] = dy
        self._cords[2] = dz

        if dz * self.speed< 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords = [i * self.speed for i in self._cords]     # расчет координат



    def get_cords(self):
         print (f"X: {self._cords[0]} <координаты по x>, Y: {self._cords[1]} <координаты по y>, Z: {self._cords[2]} <координаты по z>")

    @staticmethod
    def attack():

        if Animal._DEGREE_OF_DANGER < 5:                 # степень опасности
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0)")


class Bird(Animal):                                 # класс описывающий птиц
    beak = True  # наличие клюва


    def lay_eggs(self):
       # расчет случайного числа в диапазоне  целых чисел от 0 до 4
        print(f"Here are(is) {random.randint(0, 4)} eggs for you")


class AquaticAnimal(Animal):            # класс описывающий плавающего животного
    Animal._DEGREE_OF_DANGER = 3


    def dive_in(self,dz):
        self.speed= int(self.speed / 2)      # Скорость движения при нырянии должна уменьшаться в 2 раза

        self._cords[2] -=(abs(dz)  * self.speed)                   # расчет координаты

class PoisonousAnimal(Animal):                        # класс описывающий ядовитых животных
    Animal._DEGREE_OF_DANGER =8


class Duckbill(Bird,AquaticAnimal, PoisonousAnimal):  # класс описывающий утконоса
    sound = 'Click-click-click'

    @staticmethod
    def speak():
        print("звук :",Duckbill.sound)


class Myclass:  # разделитель
        @staticmethod
        def staticmethod():
            print("\033[33m", "_" * 20, "\033[0m")



print("\033[34m","Задача Ошибка эволюции :","\033[0m","\n","\033[33m","_" * 20,"\033[0m")

db = Duckbill(10)

print(db.live)
print(db.beak)

Myclass.staticmethod()              # разделитель

db.speak()
db.attack()

Myclass.staticmethod()              # разделитель

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

Myclass.staticmethod()              # разделитель

db.lay_eggs()