import json
from datetime import datetime
from django.utils import timezone
from time import time

from django.core.management.base import BaseCommand, CommandError
from polls.models import Question, Choice, QuestionInfo


class Command(BaseCommand):
    help = 'Import Questions from file'

    def _handle(self, *args, **options):
        """
        {"choices": [["Choice 0 0", 9], ["Choice 0 1", 7],
                     ["Choice 0 2", 10], ["Choice 0 3", 11]],
                     "author": "Author 0", "value": 30, "question_text": "Question N 0"}
        :param args:
        :param options:
        :return:
        """
        file_name = 'questions_data.json'
        with open(file_name, 'r') as outfile:
            questions = json.load(outfile)

        start = time()
        print(len(questions))
        n = 0

        for question in questions:
            q = Question.objects.create(question_text=question['question_text'])
            QuestionInfo.objects.create(question=q, author=question['author'], value=question['value'])
            [Choice.objects.create(choice_text=text, votes=votes, question=q)
             for text, votes in question['choices']]
            n += 1
            if n % 50 == 0:
                print(n)

        self.stdout.write(self.style.SUCCESS('Successfully imported. Time "%s"' % time() - start))

    def handle(self, *args, **options):
        """
        {"choices": [["Choice 0 0", 9], ["Choice 0 1", 7],
                     ["Choice 0 2", 10], ["Choice 0 3", 11]],
                     "author": "Author 0", "value": 30, "question_text": "Question N 0"}
        :param args:
        :param options:
        :return:
        """
        file_name = 'questions_data.json'
        with open(file_name, 'r') as outfile:
            questions = json.load(outfile)

        start = time()
        print(len(questions))
        n = 0
        questions_to_insert = []
        questions_dict = {}
        n_id = 1
        for question in questions:
            questions_to_insert.append(
                Question(
                    question_text=question['question_text'],
                    id=n_id
                )
            )
            questions_dict[n_id] = question
            n_id += 1

        Question.objects.bulk_create(questions_to_insert, batch_size=1000)

        questions = Question.objects.all()

        for record in queryset_iterator(questions):
            choices = []
            question_info = []
            for question in record:
                question_data = questions_dict[question.id]
                choices.extend(
                    [Choice(choice_text=text, votes=votes, question=question)
                     for text, votes in question_data['choices']]
                )
                question_info.append(
                    QuestionInfo(author=question_data['author'], question=question, value=question_data['value']))

            Choice.objects.bulk_create(choices, 1000)
            QuestionInfo.objects.bulk_create(question_info)
            n += 1000
            print(n)

        self.stdout.write(self.style.SUCCESS('Successfully imported. Time "%s"' % (time() - start)))


def queryset_iterator(queryset, chunksize=1000):
    pk = 0
    last_pk = queryset.order_by('-pk')[0].pk
    queryset = queryset.order_by('pk')
    while pk < last_pk:
        chunk = list(queryset.filter(pk__gt=pk)[:chunksize])
        pk = chunk[-1].pk
        yield chunk