from django.contrib import admin
from .models import Trade

class TradeAdmin(admin.ModelAdmin):
    list_display = ['ticker', 'quantity', 'purchase_date', 'initial_share_price']
    search_fields = ['ticker', 'quantity']
    list_filter = ['ticker']
    list_per_page = 10

admin.site.register(Trade, TradeAdmin)
