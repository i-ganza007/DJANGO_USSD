from Inner.models import Transactions
from django.core.management.base import BaseCommand

class TransactionCreater(BaseCommand):
    help = 'Creating 5 transactions'

    def handle(self, *args, **options):
        pass
        