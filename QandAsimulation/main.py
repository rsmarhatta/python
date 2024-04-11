from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
#creating questions
for i in range (0,len(question_data)):

    new_question = Question(question_data[i]["question"],question_data[i]["correct_answer"])
    question_bank.append(new_question)

#print(question_bank[0].text)
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(f"Congrats! You finished the quiz\nYour final score was {quiz.score}/{len(quiz.question_list)}")