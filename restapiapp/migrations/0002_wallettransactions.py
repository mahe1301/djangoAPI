

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restapiapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WalletTransactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_balance', models.IntegerField()),
                ('transaction_type', models.CharField(max_length=8)),
                ('transaction_amount', models.IntegerField()),
                ('transaction_status', models.CharField(max_length=8)),
                ('reference_id', models.CharField(max_length=200, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('transaction_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('wallet_info', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='restapiapp.wallet')),
            ],
            options={
                'db_table': 'WalletTransactions',
            },
        ),
    ]
