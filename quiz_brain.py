class QuizBrain:
    def __init__(self,question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0
        self.name = input("What's your name: ").title()
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        question = current_question.question
        print('-'*40)
        print(f'The difficulty of this quiz is: {current_question.difficulty}')
        print('-'*40)
        number_list = 1
        print(f"Q.{self.question_number}: {question}  ")
        print(f'Choose the correct answer: ')
        for choice in current_question.generete_list:
            print(f'[{number_list}]: {choice}. ')
            number_list += 1
        print(f'pssssssssss correct answer is: {current_question.correct_answer}') # for testing my code remove it later on
        user_answer = input('Type your answer here: -> ').title()
        self.check_correct_answer(user_answer,current_question.correct_answer)
    def has_question_left(self):
        return self.question_number < len(self.question_list)

    def check_correct_answer(self,user_answer,correct_answer):
        if user_answer == correct_answer.title():
            print(f'You get it right!')
            self.score += 1
        else:
            print(f'Your answer is wrong!')
        print(f'Your score: {self.score} / {len(self.question_list)}')
