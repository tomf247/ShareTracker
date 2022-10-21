from django.db import models
from django.contrib.auth.models import User
import datetime
from yahoo_fin import stock_info as si
from decimal import Decimal
from django.db.models import Sum, F

class Trade(models.Model):
    ''' Required fields to record the trade and derive calculations for display. '''
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    ticker = models.CharField(max_length=10)
    company_name = models.CharField(max_length=50,null=True)
    share_currency = models.CharField(max_length=3,null=True)
    quantity = models.PositiveIntegerField(null=False)
    purchase_date = models.DateField(("Date"), default=datetime.date.today)
    initial_share_price = models.DecimalField(null=False,max_digits=15,decimal_places=5)
    initial_share_value = models.DecimalField(null=False,max_digits=15,decimal_places=2)
    class Meta:
        ''' Sort by ticker symbol. '''
        ordering = ['ticker']

    def __str__(self):

        return self.ticker

    @property
    def latest_share_price(self):
        ''' API call to Yahoo Finance for latest price. '''

        handle = si.get_quote_data(str(self.ticker))
        latest_share_price = handle.get('regularMarketPrice')
        return latest_share_price

    @property
    def latest_share_value(self):
        ''' The market price multiplied by number of shares to show latest value.'''
        latest_share_value = Decimal(self.latest_share_price) * self.quantity
        return self.latest_share_price * self.quantity

    @property
    def latest_gain_loss(self):
        ''' The market value minus the initial value gives us a profit or loss.'''
        return Decimal(self.latest_share_value) - self.initial_share_value

    def save(self, *args, **kwargs):
        ''' Override default Save method to populate calculated fields. '''

        self.initial_share_value = self.initial_share_price * self.quantity
        handle = si.get_quote_data(str(self.ticker))
        self.company_name = handle.get('shortName')
        self.share_currency = handle.get('currency')
        self.ticker = self.ticker.upper()
        super().save(*args, **kwargs)
