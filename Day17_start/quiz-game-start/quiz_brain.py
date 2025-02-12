class Quizbrain:
    def __init__(self, q_bank):
        self.question_number = 0
        self.question_list = q_bank
        self.score = 0

    def still_has_questions(self):
        if self.question_number == len(self.question_list):
            return False
        return True

    def give_question(self):
        user_answer = input(f"Q.{self.question_number + 1} -- {self.question_list[self.question_number].text} (True/False): ")
        self.check_answer(user_answer)

    def check_answer(self, q_answer):
        if q_answer.lower() == self.question_list[self.question_number].answer.lower():
            print("That is correct")
            self.score += 1
        else:
            print("uuuh you are wrong")

        print(f"The correct answer was {self.question_list[self.question_number].answer}")
        self.question_number += 1
        print(f"Your current score is: {self.score}/{self.question_number}\n")

