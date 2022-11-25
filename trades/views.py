from trades.models import Trade
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from trades.forms import TradeForm
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Sum
from django.db import models
from decimal import Decimal


class ViewTrades (LoginRequiredMixin, ListView):
    ''' Display a list of all trades in the user's portfolio. '''

    model = Trade
    paginate_by = 6

    def get_queryset(self):
        ''' Selct only trades in database that are in the user's portfolio. '''

        return Trade.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        ''' Override to get a running total of the initial balance '''

        context = super(ViewTrades, self).get_context_data(*args, **kwargs)
        context['opening_balance'] = Trade.objects.filter(user=self.request.user).aggregate(Sum('initial_share_value'))
        context['latest_value'] = 1000

        return context


class CreateTrade(LoginRequiredMixin, CreateView):
    ''' Record a new trade. '''

    model = Trade
    form_class = TradeForm

    def form_valid(self, form):
        ''' Ensure the trade is saved to the user's (not someone else's) account. '''

        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        ''' Notify the Create was successful and return to the ListView '''

        messages.success(self.request, 'Trade created successfully.')
        return reverse_lazy('viewtrades')


class UpdateTrade(LoginRequiredMixin, UpdateView):
    ''' Make changes to a previously inserted trade. '''

    model = Trade
    form_class = TradeForm

    def dispatch(self, request, *args, **kwargs):
        ''' Override to ensure the user can only change their trades. '''

        handler = super(UpdateTrade, self).dispatch(request, *args, **kwargs)
        if self.object.user != request.user:
            raise Http404('You tried to update a trade that is not in your portfolio.')
        return handler

    def form_valid(self, form):
        ''' Save the changes back to the database. '''

        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        ''' Notify the Update was successful and return to the ListView '''

        messages.success(self.request, 'Trade updated successfully.')
        return reverse_lazy('viewtrades')


class DeleteTrade(LoginRequiredMixin, DeleteView):
    ''' Remove a trade from user's portfolio. '''
    model = Trade
    success_url = reverse_lazy('viewtrades')

    def dispatch(self, request, *args, **kwargs):
        ''' Override to ensure the user can only delete their trades. '''
        handler = super(DeleteTrade, self).dispatch(request, *args, **kwargs)
        if self.object.user != request.user:
            raise Http404('You tried to delete a trade that is not in your portfolio.')
        return handler

    def delete(self, request, *args, **kwargs):
        ''' Override to raise notification of successful delete. '''
        messages.success(self.request, 'Trade deleted successfully.')
        return super(DeleteTrade, self).delete(request, *args, **kwargs)


class TradeDetail(DetailView):
    ''' Display additional details for a single trade. '''
    model = Trade

    def get_context_data(self, **kwargs):
        ''' Obtain a context to return to user. '''
        context = super().get_context_data(**kwargs)
        return context
