class Living_farm:
    breath = 'alive'
    kind = 'какое-то животное'

    def breathing(self):
        print('Раз дышит, значит живое')
        return 'Работаем дальше'

    def find_type(self):
        return self.kind
        pass

class animals(Living_farm):
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight
        self.status = 'голодный'
        self.sounds = 'какие-то звуки'

    def call(self):
        return self.name

    def weigh(self):
        return self.weight

    def feed(self):
        if self.status == 'голодный':
            print(f'Покормили {self.name}')
            self.status = 'накормлено'
        else:
            print(f'Сначала накорми {self.name}, потом получай пользу')
        return self.status

    def listen_voices(self):
        if self.sounds == 'Му-му':
            self.kind = 'Корова'
            print('Мычит, значит корова')
        elif self.sounds == 'Ме-ме':
            self.kind = 'Коза'
            print('Мекает, значит коза')
        elif self.sounds == 'Беее':
            self.kind = 'Овца'
            print('Блеет, значит овца')
        elif self.sounds == 'Ко-ко-ко':
            self.kind = 'Курица'
            print('Квохчет, значит курица')
        elif self.sounds == 'Кря-кря':
            self.kind = 'Утка'
            print('Крякает, значит утка')
        elif self.sounds == 'Га-Га':
            self.kind = 'Гусь'
            print('Гогочет, значит гусь')
        else:
            print('Кто-то новенький на ферме')
        return f'Вас выслушали'

class birds(animals):
    def __init__(self, name: str, weight: int):
        super(birds, self).__init__(name, weight)
        self.eggs = 0

    def pick_eggs(self, value):
        if self.status == 'голодный':
            print(f'Сначала покорми животину {self.name} и потом будут тебе яйца')
        else:
           self.eggs = value
           return f'От птицы {self.name} собрали яиц {self.eggs} штука'

class giving_milk(animals):
    def __init__(self, name: str, weight: int):
        super(giving_milk, self).__init__(name, weight)
        self.milk = 0

    def get_milk(self, value):
        if self.status == 'голодный':
            print(f'Сначала покорми животину {self.name} и потом будет тебе молоко')
        else:
            self.milk = value
        return f'От животины {self.name} надоили молока {self.milk} литров'

class giving_wool(animals):
    def __init__(self, name: str, weight: int):
        super(giving_wool, self).__init__(name, weight)
        self.wool = 'Обросло'

    def shear(self):
        print(f'Пришла весна и {self.name} подстригли')
        self.wool = 'Подстрижено'
        return self.wool

class sheep(giving_wool):
    def __init__(self, name: str, weight: int):
        super(sheep, self).__init__(name, weight)
        self.sounds = 'Беее'

class cow(giving_milk):
    def __init__(self, name: str, weight: int):
        super(cow, self).__init__(name, weight)
        self.sounds = 'Му-му'

class goat(giving_milk):
    def __init__(self, name: str, weight: int):
        super(goat, self).__init__(name, weight)
        self.sounds = 'Ме-ме'

class goose(birds):
    def __init__(self, name: str, weight: int):
        super(goose, self).__init__(name, weight)
        self.sounds = 'Га-Га'

class hen(birds):
    def __init__(self, name: str, weight: int):
        super(hen, self).__init__(name, weight)
        self.sounds = 'Ко-ко-ко'

class duck(birds):
    def __init__(self, name: str, weight: int):
        super(duck, self).__init__(name, weight)
        self.sounds = 'Кря-кря'

animal_1 = goose('Серый', 2)
animal_2 = goose('Белый', 3)
animal_3 = hen('Ко-Ко', 1)
animal_4 = hen('Кукареку', 1)
animal_5 = duck('Кряква', 1)
animal_6 = cow('Манька', 700)
animal_7 = goat('Рога', 70)
animal_8 = goat('Копыта', 50)
animal_9 = sheep('Барашек', 100)
animal_10 = sheep('Кудрявый', 60)

animals = [animal_1, animal_2, animal_3, animal_4, animal_5, animal_6, animal_7, animal_8, animal_9, animal_10]

def all_methods_animals():
    for animal in animals:
        #print(animal.__dict__)
        #print(animal.breathing())
        print(f'Имя животного - {animal.name}, его вес - {animal.weight} кг.')
    for animal in animals:
        print(animal.listen_voices())
        print(animal.find_type())
        print(animal.feed())
        if animal.find_type() == 'Утка' or animal.find_type() == 'Курица' or animal.find_type() == 'Гусь':
            print(animal.pick_eggs(1))
        elif animal.find_type() == 'Корова' or animal.find_type() == 'Коза':
            print(animal.get_milk(3))
        elif animal.find_type() == 'Овца':
            print(animal.shear())

all_methods_animals()

def total_weight(animals):
    wt_sum = 0
    for animal in animals:
        wt_sum += animal.weight
    print(f'\n Общий вес всех живоных фермы {wt_sum} кг.')
    return wt_sum

total_weight(animals)

def wt_max(animals):
    animals_wt = {}
    for animal in animals:
        animals_wt.setdefault((animal.name), [])
        animals_wt[(animal.name)].append(animal.weight)
    for name, weight in animals_wt.items():
        wt_max = max(animals_wt, key=animals_wt.get)
    print(f'Животное фермы, имеющее максимальный вес зовут {wt_max}')

wt_max(animals)
