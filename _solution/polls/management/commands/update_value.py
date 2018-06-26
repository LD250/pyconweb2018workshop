from django.db import connection
from django.core.management.base import BaseCommand
from django.db.models import F

from polls.models import QuestionInfo


class Command(BaseCommand):
    help = 'Update choice value'

    def handle(self, *args, **options):
        #for question in QuestionInfo.objects.all():
        #    question.value = question.value * question.id
        #    question.save()
        QuestionInfo.objects.update(value=F('value') * F('id'))
        print(connection.queries[-1])
