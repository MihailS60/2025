class Animal:
    alive = True            # живой
    fed = False             # накормленный

    def __init__(self,name):
        self.name=name
        return


    def eat(self, food):

        if food.edible != True:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False
        else:
            print(f'{self.name} съел {food.name}')
            self.fed = True

class Mammal(Animal):                       # Млекопитающие
    pass

class Predator(Animal):                       #   Хищник
    pass

class Plant:
                  # съедобность)

    def __init__(self,name):
        self.name=name
        return


class Fruit(Plant):
        edible = True           # съедобность)


class Flower(Plant):
        edible = False


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)

a1.eat(p1)
a2.eat(p2)

print(a1.alive)
# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.
print(a2.fed)
