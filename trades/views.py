from trades.models import Trade
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

class ViewTrades (LoginRequiredMixin, ListView):

    model = Trade
    paginate_by = 6

    def get_queryset(self):

        return Trade.objects.filter(user=self.request.user)
