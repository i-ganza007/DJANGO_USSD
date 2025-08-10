from django.core.management.base import BaseCommand
from Inner.models import PrimaryUser

class Command(BaseCommand):
    help = 'Creating Users'

    def handle(self, *args, **options):
        inits = [
            {'code_name': 'TenHag', 'age': 40, 'maj_currency': 'USD', 'phone': 788528594, 'pin': 7777},
            {'code_name': 'Trost', 'age': 29, 'maj_currency': 'EUR', 'phone': 791803813, 'pin': 2811},
            {'code_name': 'Benimare', 'age': 20, 'maj_currency': 'KSH', 'phone': 783435706, 'pin': 0000},
            {'code_name': 'Elmo', 'age': 24, 'maj_currency': 'UGX', 'phone': 737359583, 'pin': 1200},
            {'code_name': 'Okra', 'age': 30, 'maj_currency': 'RWF', 'phone': 782189006, 'pin': 9200},
        ]

        arr = []
        for init in inits:
            arr.append(PrimaryUser(**init))
            print(self.stdout.write(self.style.SUCCESS(f'Added {init['code_name']}')))

        PrimaryUser.objects.bulk_create(arr) 


