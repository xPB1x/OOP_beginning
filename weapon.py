class MeleeWeapon:

    def __init__(self, name):
        self.name = name
        self.strength = 100
    # Метод родительского класса.

    def slashing_blow(self):
        # При рубящем ударе уменьшаем прочность меча на 10.
        self.strength -= 10
        return f'Нанесён рубящий удар оружием {self.name}.'

    def sharpen(self):
        self.strength = 100
        return (f'Оружие "{self.name}" заточено.')


class Sword(MeleeWeapon):

    # Переопределяем метод родительского класса...
    def slashing_blow(self):
        # ...меняем значение снижения прочности...
        self.strength -= 5
        # ...и меняем сообщение.
        return f'Мечом {self.name} был нанесен рубящий удар.'

    def piercing_strike(self):
        self.strength -= 5
        return f'Нанесён пронзающий удар мечом {self.name}.'


class Axe(MeleeWeapon):
    ...


brodex = Axe('Верный')
xiphos = Sword('Разящий')

print(xiphos.slashing_blow())
print(xiphos.strength)
print(brodex.slashing_blow())
print(brodex.strength)
