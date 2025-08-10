from Inner.models import Transactions , PrimaryUser
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Creating  transactions'

    def handle(self, *args, **options):
        first_user = PrimaryUser.objects.get(id=1)
        second_user = PrimaryUser.objects.get(id=2)
        third_user = PrimaryUser.objects.get(id=3)
        fourth_user = PrimaryUser.objects.get(id=4)
        fifth_user = PrimaryUser.objects.get(id=5)

        trans = [
            {'sender':first_user,'receiver':791803813,'amount':20300},
            {'sender':first_user,'receiver':791803813,'amount':21300},
            {'sender':second_user,'receiver':783435706,'amount':1000},
            {'sender':second_user,'receiver':783435706,'amount':900},
            {'sender':third_user,'receiver':737359583,'amount':200000},
            {'sender':third_user,'receiver':737359583,'amount':1320},
            {'sender':fourth_user,'receiver':782189006,'amount':790},
            {'sender':fourth_user,'receiver':782189006,'amount':400},
            {'sender':fifth_user,'receiver':782189006,'amount':90000},
            {'sender':fifth_user,'receiver':782189006,'amount':50124}
        ]

        oper = []

        for tran in trans:
            oper.append(Transactions(**tran))
            print(self.stdout.write(self.style.SUCCESS(f'Sent from {tran['sender']} to {tran['receiver']} with {tran['amount']}')))
        Transactions.objects.bulk_create(oper)
        