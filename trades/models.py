from django.db import models
from django.contrib.auth.models import User
import datetime

class Trade(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    ticker = models.CharField(max_length=10)
    company_name = models.CharField(max_length=40,null=True)
    share_currency = models.CharField(max_length=3,null=True)
    quantity = models.PositiveIntegerField(null=False)
    purchase_date = models.DateField(("Date"), default=datetime.date.today)
    initial_share_price = models.DecimalField(null=False,max_digits=15,decimal_places=5)
    initial_share_value = models.DecimalField(null=False,max_digits=15,decimal_places=2)
    latest_share_price = models.DecimalField(null=True,max_digits=15,decimal_places=5)
    latest_share_value = models.DecimalField(null=True,max_digits=15,decimal_places=2)
    latest_gain_loss = models.DecimalField(null=True,max_digits=15,decimal_places=2)

    class Meta:
        ordering = ['ticker']

    def __str__(self):

        return self.ticker
