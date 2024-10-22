class QuizBrain:
    def __init__(self, questions):
        self.question_no = 0
        self.question_list = questions
        self.score = 0

    def still_has_questions(self):
        return len(self.question_list) > self.question_no

    def nextQuestion(self):
        question_item = self.question_list[self.question_no]
        self.question_no += 1
        user_input = input(f"Q.{self.question_no}: {question_item.text} (True/False): ")
        self.checkAnswer(user_input, question_item.answer)

    def checkAnswer(self, user_input, correct_answer):
        if user_input.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("You got it wrong!")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_no}")