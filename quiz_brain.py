class QuizzNumber:
    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def check_difficulty(self):
        chosen_difficulty = input("What difficulty fits you? (easy|medium|hard): ").lower()
        self.questions_list = [q for q in self.questions_list if q.difficulty == chosen_difficulty]

    def check_answers(self, input_given, answer_given):
        question_item = self.questions_list[self.question_number]
        if input_given.lower() == answer_given.lower():
            print(f"The answer was {question_item.answer}, Good Job!")
            self.question_number += 1
            self.score += 1
        else:
            print(f"The answer was {question_item.answer}, That is a wrong answer....")
            self.question_number += 1

        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")

    def final_score(self):
        print(f"You've completed this quiz!\nYour final score is: {int(self.score)}/{int(self.question_number)}")

    def next_question(self):
        if self.still_has_questions():
            question_item = self.questions_list[self.question_number]
            user_answer = input(f"{question_item.text} (True/False): ")
            self.check_answers(user_answer, question_item.answer)
        else:
            print("No more questions available.")
