from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.create_admin()

    def create_admin(self):
        if not User.objects.filter(username="swruler").exists():
            User.objects.create_superuser("swruler", "admin@softworks.com.my", 
                                          "sw will rule the world")
