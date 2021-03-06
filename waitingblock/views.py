from django.db import models
from django_tables2 import MultiTableMixin, RequestConfig
from django.views.generic import TemplateView, CreateView, UpdateView, FormView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from django.contrib.auth.forms import UserCreationForm
from django.views import generic

from .models import Customer
from .tables import CustomerTable, CustomerUpdateTable
from .forms import CustomerForm, CustomerUpdateForm

#from .filters import CustomerListFilter
#from .utils import PagedFilteredTableView


class WaitingblockView(FormView, TemplateView):
    model = Customer
    template_name = 'waitingblock/base.html'
    context_object_name = 'customer'
    form_class = CustomerForm

    def form_valid(self, form):
        form.save()
        return redirect('home')

    def redirect_view(request):
        response = redirect('home')
        return response


class CustomerUpdateView(MultiTableMixin, UpdateView):
    model = Customer
    template_name = 'waitingblock/customer_update_form.html'
    context_object_name = 'customer'
    order_by_field = ['arrival_time']
    pk_url_kwarg = 'customer_pk'
    table_pagination = {'per_page': 1}
    table_class = CustomerUpdateTable
    table_data = Customer.objects.all()
    form_class = CustomerUpdateForm
    is_seated = models.BooleanField()

    def get_tables(self):
        qs = Customer.objects.all()
        return [CustomerUpdateTable(qs, exclude=(
            'unique_id',
            'contact',
        ))]

    def get_object(self):
        return self.request.user

    def seat(self):
        Customer.objects.status() == False
        self.save()
        response = redirect('tables/')
        return response

    def form_valid(self, form):
        form.save(self.request.user)
        return super(CustomerUpdateView, self).form_valid(form)

    def redirect_view(request):
        response = redirect('tables/')
        return response

    def get_success_url(self):
        return ('success/')


class TablesView(MultiTableMixin, FormView, TemplateView):
    model = Customer
    template_name = 'waitingblock/tables.html'
    context_object_name = 'customer'
    table_pagination = {'per_page': 5}
    order_by_field = ['arrival_time']
    pk_url_kwarg = 'customer_pk'
    table_class = CustomerTable
    table_data = Customer.objects.all()
    #    filter_class = CustomerListFilter
    form_class = CustomerForm

    def get_tables(self, *args, **kwargs):
        qs = Customer.objects.all()
        return [
            CustomerTable(
                qs, exclude=('unique_id', 'arrival_time', 'contact'))
        ]

    def form_valid(self, form):
        form.save(self.request.user)
        return super(TablesView, self).form_valid(form)


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class PasswordReset(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('password_reset')


#    template_name = 'registration/password_reset_form.html'
