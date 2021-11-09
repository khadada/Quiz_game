from question_module import Question
from data import data_quiz , logo
from quiz_brain import QuizBrain
from prettytable import PrettyTable
print(logo)
user_summary = PrettyTable()
question_bank = []
for question in data_quiz:
    new_question = Question(question['category'],question['type'],question['difficulty'],question['question'],question['correct_answer'],question['incorrect_answers'])
    new_question.generete_list_answer()
    question_bank.append(new_question)
quiz_one = QuizBrain(question_bank)

while quiz_one.has_question_left():
    quiz_one.next_question()

user_summary.add_column('Name ',[f'{quiz_one.name}'])
user_summary.add_column('Score ',[f'{quiz_one.score} / {len(quiz_one.question_list)}'])
print(logo)
print(user_summary)
