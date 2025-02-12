from data import question_data
from question_model import Question
from quiz_brain import Quizbrain

question_bank = []

for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"]))

quiz = Quizbrain(question_bank)

while quiz.still_has_questions():
    quiz.give_question()
print("You've completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
