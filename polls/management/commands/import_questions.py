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
        start = time()
        self.stdout.write(self.style.SUCCESS('Successfully imported. Time "%s"' % time() - start))

