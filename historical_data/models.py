from django.db import models


# Model Finance_data object
class FinanceData(models.Model):
    id = models.AutoField(primary_key=True)
    symbol = models.CharField(max_length=5, default='None')
    date = models.DateField(verbose_name='Date', unique=True)
    open = models.FloatField(verbose_name='Open')
    high = models.FloatField(verbose_name='High')
    low = models.FloatField(verbose_name='Low')
    close = models.FloatField(verbose_name='Close*')
    adj_close = models.FloatField(verbose_name='Adj CLose**')
    volume = models.IntegerField(verbose_name='Volume')

    def __str__(self):
        return self.symbol
