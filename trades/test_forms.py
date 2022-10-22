from django.test import TestCase
from .forms import TradeForm


class TestForms(TestCase):

    def test_ticker_is_present(self):
        form = TradeForm({'ticker': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('ticker', form.errors.keys())
        self.assertEqual(form.errors['ticker'][0], 'This field is required.')

    def test_ticker_is_present_but_invalid(self):
        form = TradeForm({'ticker': '%£%)_'})
        self.assertFalse(form.is_valid())
        self.assertIn('ticker', form.errors.keys())
        self.assertEqual(form.errors['ticker'][0], 'Invalid Ticker Symbol.')

    def test_quantity_is_present(self):
        form = TradeForm({'quantity': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('quantity', form.errors.keys())
        self.assertEqual(form.errors['quantity'][0], 'This field is required.')

    def test_quantity_is_present_but_invalid(self):
        form = TradeForm({'quantity': '!"£"df%'})
        self.assertFalse(form.is_valid())
        self.assertIn('quantity', form.errors.keys())
        self.assertEqual(form.errors['quantity'][0], 'Enter a whole number.')

    def test_quantity_is_positive(self):
        form = TradeForm({'quantity': '-10'})
        self.assertFalse(form.is_valid())
        self.assertIn('quantity', form.errors.keys())
        self.assertEqual(form.errors['quantity'][0], 'Ensure this value is greater than or equal to 0.')

    def test_purchase_date_is_present(self):
        form = TradeForm({'purchase_date': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('purchase_date', form.errors.keys())
        self.assertEqual(form.errors['purchase_date'][0], 'This field is required.')

    def test_purchase_date_is_present_but_invalid(self):
        form = TradeForm({'purchase_date': '&*^&^*&'})
        self.assertFalse(form.is_valid())
        self.assertIn('purchase_date', form.errors.keys())
        self.assertEqual(form.errors['purchase_date'][0], 'Enter a valid date.')

    def test_initial_share_price_is_present(self):
        form = TradeForm({'initial_share_price': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('initial_share_price', form.errors.keys())
        self.assertEqual(form.errors['initial_share_price'][0], 'This field is required.')

    def test_initial_share_price_is_present_but_invalid(self):
        form = TradeForm({'initial_share_price': 'sdf78h'})
        self.assertFalse(form.is_valid())
        self.assertIn('initial_share_price', form.errors.keys())
        self.assertEqual(form.errors['initial_share_price'][0], 'Enter a number.')

    def test_initial_share_price_is_positive(self):
        form = TradeForm({'initial_share_price': '-10'})
        self.assertFalse(form.is_valid())
        self.assertIn('initial_share_price', form.errors.keys())
        self.assertEqual(form.errors['initial_share_price'][0], 'The share price must be greater than 0.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = TradeForm()
        self.assertEqual(form.Meta.fields, ['ticker', 'quantity', 'purchase_date', 'initial_share_price'])
