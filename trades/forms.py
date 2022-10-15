from django import forms
from django.forms import ModelForm
from trades.models import Trade


class DateInput(forms.DateInput):
    input_type = 'date'


class TradeForm(forms.ModelForm):
    class Meta:
        model = Trade
        fields = '__all__'
        widgets = {
        'purchase_date': DateInput()
        }