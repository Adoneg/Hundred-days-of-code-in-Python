from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    text = item['question']
    answer = item['correct_answer']
    question_bank.append(Question(text, answer))

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
if quiz.score >8:
    print("You did excellent!")