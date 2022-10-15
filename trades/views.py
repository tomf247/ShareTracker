from trades.models import Trade
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from trades.forms import TradeForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages

class ViewTrades (LoginRequiredMixin, ListView):
    ''' Display a list of all shares purchased for the logged in user '''

    model = Trade
    paginate_by = 6

    def get_queryset(self):

        return Trade.objects.filter(user=self.request.user)

class CreateTrade(CreateView):
    ''' Record a new share purchase '''

    model = Trade
    form_class = TradeForm

    def form_valid(self, form):
        ''' Ensure the trade is saved to the user's account  '''
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, 'Trade created successfully')
        return reverse_lazy('viewtrades')
