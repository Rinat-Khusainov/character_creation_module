from random import randint


class Character:
    BRIEF_DESC_CHAR_CLASS = 'отважный любитель приключений'

    def __init__(self, char_name: str, char_class: str):
        self.char_name = char_name
        self.char_class = char_class

    def __str__(self):
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя. '
          'Сильный, выносливый и отважный.')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя. '
            'Обладает высоким интеллектом.')
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель. '
            'Черпает силы из природы, веры и духов.')
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}.'

    def attack(self):
        pass

    def defence(self):
        pass

    def special(self):
        pass


class Warrior(Character):
    def __init__(self, char_name: str):
        super().__init__(char_name, 'Warrior')

    def attack(self):
        return f'{self.char_name} нанёс противнику урон, равный {5 + randint(3, 5)}'

    def defence(self):
        return f'{self.char_name} блокировал {10 + randint(5, 10)} ед. урона'

    def special(self):
        return f'{self.char_name} применил специальное умение «Выносливость {80 + 25}»'


class Mage(Character):
    def __init__(self, char_name: str):
        super().__init__(char_name, 'Mage')

    def attack(self):
        return f'{self.char_name} нанёс противнику урон, равный {5 + randint(5, 10)}'

    def defence(self):
        return f'{self.char_name} блокировал {10 + randint(-2, 2)} ед. урона'

    def special(self):
        return f'{self.char_name} применил специальное умение «Атака {5 + 40}»'


class Healer(Character):
    def __init__(self, char_name: str):
        super().__init__(char_name, 'Healer')

    def attack(self):
        return f'{self.char_name} нанёс противнику урон, равный {5 + randint(-3, -1)}'

    def defence(self):
        return f'{self.char_name} блокировал {10 + randint(2, 5)} ед. урона'

    def special(self):
        return f'{self.char_name} применил специальное умение «Защита {10 + 30}»'


warrior = Warrior('Arnold')
print(warrior)
print(warrior.attack())
