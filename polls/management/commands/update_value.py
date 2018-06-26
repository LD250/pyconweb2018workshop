from django.db import connection
from django.core.management.base import BaseCommand
from django.db.models import F

from polls.models import QuestionInfo


class Command(BaseCommand):
    help = 'Update choice value'

    def handle(self, *args, **options):
        pass
