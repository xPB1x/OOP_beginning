class Bird:

    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size

    def describe(self, full=False):
        return f'Размер птицы {self.name} - {self.size}'


class Parrot(Bird):
    def __init__(self, name, size, color) -> None:
        super().__init__(name, size)
        self.color = color

    def describe(self, full=False):
        if full:
            return (f'Попугай {self.name} — заметная птица, '
                    f'окрас её перьев — {self.color}, '
                    f'размер — {self.size}. '
                    f'Интересный факт: попугаи чувствуют ритм, '
                    f'а вовсе не бездумно двигаются под музыку. '
                    f'Если сменить композицию, '
                    f'то и темп движений птицы изменится. ')
        return super().describe(full)

    def repeat(self, phrase):
        return f'Попугай {self.name} говорит {phrase}.'


class Penguin(Bird):
    def __init__(self, name, size, genus) -> None:
        super().__init__(name, size)
        self.genus = genus

    def describe(self, full=False):
        if full:
            return (f'Размер пингвина {self.name} '
                    f'из рода {self.genus} — {self.size}. '
                    f'Интересный факт: однажды группа геологов-разведчиков '
                    f'похитила пингвинье яйцо, и их принялась преследовать '
                    f'вся стая, не пытаясь, впрочем, при этом нападать. '
                    f'Посовещавшись, похитители вернули птицам яйцо, '
                    f'и те отстали.')
        return super().describe(full)

    def swimming(self):
        return f'Попугай {self.name} плавает со средней скоростью 11 км/ч'


kesha = Parrot('Ара', 'средний', 'красный')
kowalski = Penguin('Королевский', 'большой', 'Aptenodytes')
print(kesha.describe(True))
print()
print(kowalski.describe(True))
