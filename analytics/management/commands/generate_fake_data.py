# analytics/management/commands/generate_fake_data.py
from django.core.management.base import BaseCommand
import pandas as pd
from faker import Faker

class Command(BaseCommand):
    help = 'Generate fake user data and save to CSV'

    def handle(self, *args, **options):
        fake = Faker()
        data = {
            "name": [fake.name() for _ in range(100)],
            "email": [fake.email() for _ in range(100)],
            "address": [fake.address() for _ in range(100)],
            "age": [fake.random_int(min=18, max=80) for _ in range(100)],
            "salary": [fake.random_int(min=30000, max=120000) for _ in range(100)],
            "phone_number": [fake.phone_number() for _ in range(100)],
            "job": [fake.job() for _ in range(100)],
        }

        df = pd.DataFrame(data)
        df.to_csv('fake_user_data.csv', index=False)

        self.stdout.write(self.style.SUCCESS('Fake data generated and saved to fake_user_data.csv'))
