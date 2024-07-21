class Human:
    def __init__(self, name) -> None:
        self.name = name

    def answer_question(self, question):
        print('Очень интересный вопрос! Не знаю.')


class Student(Human):
    def __init__(self, name) -> None:
        super().__init__(name)

    def ask_question(self, Human, question):
        print(f'{Human.name}, {question}')
        Human.answer_question(question)
        print()


class Mentor(Human):
    def __init__(self, name) -> None:
        super().__init__(name)

    def answer_question(self, question):
        if question in question_list:
            if question == question_list[0]:
                print('Отдохни и возвращайся с вопросами по теории.')
                return
            if question == question_list[2]:
                print('Сейчас расскажу.')
                return
        return super().answer_question(question)


class Curator(Human):
    def __init__(self, name) -> None:
        super().__init__(name)

    def answer_question(self, question):
        if question in question_list:
            if question == question_list[0]:
                print('Держись, всё получится. Хочешь видео с котиками?')
                return
            if question == question_list[2]:
                print('Сейчас расскажу.')
                return
        return super().answer_question(question)


class CodeReviewer(Human):
    def __init__(self, name) -> None:
        super().__init__(name)

    def answer_question(self, question):
        if question in question_list:
            if question == question_list[0]:
                print('Держись, всё получится. Хочешь видео с котиками?')
                return
            if question == question_list[1]:
                print('О, вопрос про проект, это я люблю.')
                return
            if question == question_list[2]:
                print('Сейчас расскажу.')
                return
        return super().answer_question(question)


question_list = ['мне грустненько, что делать?',
                 'что не так с моим проектом?',
                 'как устроиться на работу питонистом?']


student1 = Student('Тимофей')
curator = Curator('Марина')
mentor = Mentor('Ира')
reviewer = CodeReviewer('Евгений')
friend = Human('Виталя')

student1.ask_question(curator, 'мне грустненько, что делать?')
student1.ask_question(mentor, 'мне грустненько, что делать?')
student1.ask_question(reviewer, 'когда каникулы?')
student1.ask_question(reviewer, 'что не так с моим проектом?')
student1.ask_question(friend, 'как устроиться на работу питонистом?')
student1.ask_question(mentor, 'как устроиться на работу питонистом?')
