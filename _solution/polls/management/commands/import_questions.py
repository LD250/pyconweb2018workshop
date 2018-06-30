import json
from datetime import datetime
from django.utils import timezone
from time import time

from django.core.management.base import BaseCommand, CommandError
from polls.models import Question, Choice, QuestionInfo


class Command(BaseCommand):
    help = 'Import Questions from file'

    def handle(self, *args, **options):
        """
        {"choices": [["Choice 0 0", 9], ["Choice 0 1", 7],
                     ["Choice 0 2", 10], ["Choice 0 3", 11]],
                     "author": "Author 0", "value": 30, "question_text": "Question N 0"}
        :param args:
        :param options:
        :return:
        """
        with open('questions_data.json') as outfile:
            questions = json.load(outfile)
        n = 0
        start = time()
        print(len(questions))

        questions_db = []
        questions_dict = {}
        for question in questions:
            questions_db.append(
                Question(
                    question_text=question['question_text']
                )
            )
            questions_dict[question['question_text']] = question
        Question.objects.bulk_create(
            questions_db,
            batch_size=10000
        )

        questions = Question.objects.all()
        for question_chunk in queryset_iterator(questions):
            choices = []
            infos = []
            for question in question_chunk:
                q = questions_dict.get(question.question_text)
                choices.extend(
                    Choice(
                        choice_text=text,
                        votes=votes,
                        question=question
                    ) for text, votes in q['choices']
                )
                infos.append(
                    QuestionInfo(
                        author=q['author'],
                        value=q['value'],
                        question=question
                    )
                )
            QuestionInfo.objects.bulk_create(infos)
            Choice.objects.bulk_create(choices, batch_size=5000)
            # if n % 50 == 0:
            #     print(n)
            n += 5000
            print(n)

        self.stdout.write(self.style.SUCCESS('Successfully imported. Time "%s"' % (time() - start)))



def queryset_iterator(queryset, chunksize=5000):
    id = 0
    last_id = queryset.order_by('-id')[0].id
    queryset = queryset.order_by('id')
    while id < last_id:
        chunk = list(queryset.filter(id__gt=id)[:chunksize])
        id = chunk[-1].id
        yield chunk
