from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    text = question["text"]
    answer = question["answer"]
    new_question = Question(text, answer)
    question_bank.append(new_question )

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the Quiz.\n Your final score was: {quiz.score}/{len(question_bank)}")

# You can visit opentdb.com and access their API to get JSON files of random trivia questions similar to the ones in our data.py file.