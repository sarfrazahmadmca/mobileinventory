from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, View
from django.views.generic.edit import CreateView
from django.contrib import messages

from .models import SalesPerson, Transactions, Customer, ItemBrandObject
from .forms import TransactionForm

from common.mixins import LoginRequiredMixin, OnlySalesPersonRequiredMixin

class CreateSalerPerson(CreateView):
    model = SalesPerson
    form_class = UserCreationForm
    template_name = 'create_sales_person.html'

    def form_valid(self,form):
        data = form.cleaned_data
        username = data['username']
        password = data['password1']
        user = User.objects.create_user(username=username, password=password)
        SalesPerson.objects.create(user=user)
        user = authenticate(username=username, password=password)
        login(self.request, user)
        messages.success(self.request, 'You have been successfully registered as a sales person')
        return HttpResponseRedirect(reverse('home', args=[user.id]))

class Home(LoginRequiredMixin,DetailView):
    model = User
    template_name = 'home.html'

    def get_object(self, queryset=None):
        return User.objects.get(id=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['customers'] = self.object.sales_person.all()
        context['transactions'] = self.object.transactions.all()
        context['products'] = ItemBrandObject.objects.all()
        return context


class AddCustomer(LoginRequiredMixin, OnlySalesPersonRequiredMixin, CreateView):
    model = Customer
    template_name = 'add_customers.html'
    form_class = UserCreationForm

    def form_valid(self,form):
        login_user = self.request.user
        data = form.cleaned_data
        username = data['username']
        password = data['password1']
        user = User.objects.create_user(username=username, password=password)
        Customer.objects.create(customer=user, sales_person=login_user)
        messages.success(self.request, 'Customer added successfully')
        return HttpResponseRedirect(reverse('home'))


class CreateTransaction(LoginRequiredMixin, OnlySalesPersonRequiredMixin, CreateView):
    model = Transactions
    template_name = 'create_transactions.html'
    form_class = TransactionForm

    def form_valid(self, form):
        user = self.request.user
        obj = form.save(commit=False)
        obj.sales_person = user
        obj.save()
        messages.success(self.request, 'Transaction is done successfully')
        return HttpResponseRedirect(reverse('home'))


class CreateProduct(LoginRequiredMixin, OnlySalesPersonRequiredMixin,CreateView):
    model = ItemBrandObject
    template_name = 'create_product.html'

    def get_success_url(self):
        return reverse('home')
    def form_valid(self, form):
         messages.success(self.request, 'Product has been added successfully')
         return super(CreateProduct, self).form_valid(form)




create_sales_person = CreateSalerPerson.as_view()
home = Home.as_view()
create_transactions = CreateTransaction.as_view()
add_customer = AddCustomer.as_view()
add_product = CreateProduct.as_view()

