from datetime import datetime


# Объявите класс Quest с методами и свойствами.
class Quest:

    def __init__(self, name, description, goal):
        self.name = name
        self.description = description
        self.goal = goal
        self.start_time = None
        self.end_time = None
        self.completion_time = None

    def accept_quest(self):
        self.start_time = datetime.now()
        if not self.end_time:
            return 'С этим квестом вы уже справились'
        return f'Начало "{self.name}" положено.'

    def pass_quest(self):
        self.end_time = datetime.now()
        if not self.start_time:
            return 'Нельзя завершить то, что не имеет начала!'
        self.completion_time = self.end_time - self.start_time
        return (f'Квест {self.name} окончен.'
                f'Время выполнения квеста: {self.completion_time}')

    def __str__(self):
        if self.completion_time is not None:
            return f'Цель квеста {self.name} - {self.goal} Квест завершён.'
        elif self.start_time:
            return f'Цель квеста {self.name} - {self.goal} Квест выполняется.'
        return f'Цель квеста {self.name} - {self.goal}'


# В этих переменных содержатся значения, которые нужно передать
# в качестве аргументов в экземпляр класса Quest.
quest_name = 'Сбор пиксельники'
quest_goal = 'Соберите 12 ягод пиксельники.'
quest_description = '''
В древнем лесу Кодоборье растёт ягода "пиксельника".
Она нужна для приготовления целебных снадобий.
Соберите 12 ягод пиксельники.'''
# Создайте экземпляр класса Quest.

new_quest = Quest(quest_name, quest_description, quest_goal)
print(new_quest)
new_quest.accept_quest()
print(new_quest)
new_quest.pass_quest()
print(new_quest)
