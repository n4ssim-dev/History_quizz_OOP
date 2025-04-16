from question_model import Question
from quiz_brain import QuizzNumber
from data import question_data

art = """
a@@@@@@@@a  a@@@@@@a  a@@@@@@@a a@@@@@@@@a a@@a.  .a@@a  a@@a
@@@@  @@@@ @@@@  @@@@ @@@@  @@@ @@@@@@@@@@ @@@@a  a@@@@  @@@@
@@@@  @@@@ @@@@  @@@@ @@@@  @@@    @@@@    `@@@@  @@@@'  @@@@
@@@@@@@@@@ @@@@@@@@@@ @@@@@@@@'    @@@@      `@@@@@@'    @@@@
@@@@@@@@@' @@@@@@@@@@ @@@@@@@@a    @@@@        @@@@      `@@'
@@@@       @@@@  @@@@ @@@@ @@@@    @@@@        @@@@
@@@@       @@@@  @@@@ @@@@ @@@@    @@@@        @@@@       @@
"""

question_bank = []

print(art)
print("Welcome to this little history Quiz!\nReady, Set, GO!\n")

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    question_difficulty = question["difficulty"]
    question_bank.append(Question(question_text, question_answer, question_difficulty))

quizz = QuizzNumber(question_bank)
quizz.check_difficulty()

while quizz.still_has_questions():
    quizz.next_question()

quizz.final_score()
