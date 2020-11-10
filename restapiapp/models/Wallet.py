from django.db import models
from . import CustomAccount


class Wallet(models.Model):
    owned_by = models.ForeignKey(CustomAccount, on_delete=models.PROTECT)
    current_balance = models.IntegerField(default=0)
    status = models.CharField(max_length=8)
    enabled_at = models.DateTimeField(blank=True,null=True)
    disabled_at = models.DateTimeField(blank=True,null=True)
    
    class Meta:
        db_table = 'Wallet'