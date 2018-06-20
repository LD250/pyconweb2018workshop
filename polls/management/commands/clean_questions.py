import json
from time import time

from django.core.management.base import BaseCommand, CommandError
from polls.models import Question


class Command(BaseCommand):
    help = 'Delete all Questions'

    def handle(self, *args, **options):
        start = time()
        Question.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Successfully deleted. Time "%s"' % (time() - start)))