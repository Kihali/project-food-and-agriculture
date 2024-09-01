from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.core.management import CommandError

class Command(BaseCommand):
    help = 'Creates a superuser with predefined credentials'

    def add_arguments(self, parser):
        parser.add_argument('--username', type=str, help='Username for the superuser')
        parser.add_argument('--email', type=str, help='Email for the superuser')
        parser.add_argument('--password', type=str, help='Password for the superuser')

    def handle(self, *args, **kwargs):
        username = kwargs['username'] or 'admin'
        email = kwargs['email'] or 'admin@example.com'
        password = kwargs['password'] or 'password'

        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING(f'Superuser {username} already exists'))
        else:
            try:
                User.objects.create_superuser(username=username, email=email, password=password)
                self.stdout.write(self.style.SUCCESS(f'Superuser {username} created successfully'))
            except Exception as e:
                raise CommandError(f'Error creating superuser: {e}')
