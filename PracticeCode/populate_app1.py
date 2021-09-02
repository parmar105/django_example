import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PracticeCode.settings')

import django
django.setup()
from app1.models import UsersInfo
from faker import Faker
fakergen = Faker()


def add_users(N=5):
    for entry in range(N):
        fake_fname = fakergen.first_name()
        fake_lname = fakergen.last_name()
        fake_email = fakergen.email()

        user = UsersInfo.objects.get_or_create(first_name=fake_fname, last_name=fake_lname, email=fake_email)


if __name__ == '__main__':
    print("populating scripts!")
    add_users(10)
    print("populating completed")

