from random import randint
import json

N = 50000

questions = []
for n in range(N):
    question = {
        'question_text': 'Question N {}'.format(n),
        'choices': [['Choice {} {}'.format(n, i), randint(1, 15)] for i in range(randint(1, 5))],
        'author': 'Author {}'.format(n),
        'value': randint(1, 55)
    }
    questions.append(question)

with open('questions_data.json', 'w') as outfile:
    json.dump(questions, outfile)
