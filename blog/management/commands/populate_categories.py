from typing import Any

from django.core.management.base import BaseCommand
from blog.models import Category


class Command(BaseCommand):
   help = "This command inserts category data"

   def handle(self, *args: Any, **options: Any):
      Category.objects.all().delete()

      categories = [
         'Technology',
         'Science',
         'Health',
         'Travel',
         'Food',
         'Finance',
         'Culture',
         'Lifestyle',
         'Career',
         'Education',
      ]

      for category_name in categories:
          Category.objects.create(name=category_name)
      self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))
