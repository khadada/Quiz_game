from random import shuffle
class Question:

    def __init__(self,category,type,difficulty,question,correct_answer, incorrect_list):
        self.category = category
        self.type = type
        self.difficulty = difficulty
        self.question = question
        self.incorrect_answers = incorrect_list
        self.correct_answer = correct_answer
        self.generete_list = []
    def generete_list_answer(self):
        text_end = ''
        for answer in self.incorrect_answers:
            text_end += f'{str(answer)}, '
        text_end += f'{self.correct_answer} '
        self.generete_list = text_end.split(', ')

