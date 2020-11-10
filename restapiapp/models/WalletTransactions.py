from django.db import models
from . import CustomAccount,Wallet


class WalletTransactions(models.Model):
    transaction_by = models.ForeignKey(CustomAccount, on_delete=models.PROTECT)
    wallet_info = models.ForeignKey(Wallet, on_delete=models.PROTECT)
    current_balance = models.IntegerField()
    transaction_type = models.CharField(max_length=10)
    transaction_amount = models.IntegerField()
    transaction_status = models.CharField(max_length=8)
    reference_id=models.CharField(max_length=200,unique=True)
    created = models.DateTimeField(auto_now_add=True,blank=True)
    
    class Meta:
        db_table = 'WalletTransactions'