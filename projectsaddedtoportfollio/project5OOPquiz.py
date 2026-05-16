score = 0

class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    def check_answer(self, userAns):
        global score
        if userAns == self.answer:
            score += 1
            print(f'Your answer is correct! Your current score is {score}.')
        elif userAns != self.answer:
            print(f'Oh No! You got it wrong! Your answer was {userAns} but the correct answer is {self.answer}. Your score is {score}.')

question1 = Question('What is 1+1? \nA: 1 \nB: 2 \nC: 3 \nD: 4 \nANS:', 'b')
answer1 = input(question1.question).lower()
question1.check_answer(answer1)
question2 = Question('What is 2+2? \nA: 1 \nB: 2 \nC: 3 \nD: 4 \nANS:', 'd')
answer2 = input(question2.question).lower()
question2.check_answer(answer2)
question3 = Question('What does x^2+y^2=1 make on a coordinate plane? \nA: circle \nB: square \nC: line \nD: parabola \nANS:', 'a')
answer3 = input(question3.question).lower()
question3.check_answer(answer3)
print(f'The quiz is over. Good job! Your final score is {score}/3')