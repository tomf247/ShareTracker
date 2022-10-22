from django import forms
from django.forms import ModelForm
from trades.models import Trade
from yahoo_fin import stock_info as si


class DateInput(forms.DateInput):
    input_type = 'date'


class TradeForm(forms.ModelForm):
    ''' Add a new Trade and check input is valid '''
    class Meta:
        model = Trade
        fields = ['ticker', 'quantity', 'purchase_date', 'initial_share_price']
        widgets = {
            'purchase_date': DateInput()
        }

    def clean_ticker(self):
        ''' Validate that ticker submitted is known on the Stock Exchange.'''

        ticker = self.cleaned_data.get('ticker')
        try:
            handle = si.get_quote_data(ticker)
        except Exception as e:
            raise forms.ValidationError('Invalid Ticker Symbol.')
        return ticker

    def clean_quantity(self):
        ''' Check the number of shares input is valid. '''
        quantity = self.cleaned_data.get('quantity')
        if (quantity <= 0):

            raise forms.ValidationError('Quantity must be greater than 0.')
        return quantity

    def clean_initial_share_price(self):
        ''' Check the price field of shares input is valid. '''

        initial_share_price = self.cleaned_data.get('initial_share_price')
        if (initial_share_price <= 0):

            raise forms.ValidationError('The share price must be more than 0.')
        return initial_share_price
