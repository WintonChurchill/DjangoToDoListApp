from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
 
 
class Command(BaseCommand):
 
    def handle(self, *args, **options):
        if not User.objects.filter(username="todoawsadmin").exists():
            User.objects.create_superuser("todoawsadmin", "georgevaughan135@gmail.com", "georges321")