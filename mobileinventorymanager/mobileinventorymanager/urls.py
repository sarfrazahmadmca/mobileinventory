from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
    # url(r'^$',TemplateView.as_view(template_name='index.html'), name='home_url'),
     url(r'^$','inventoryapp.views.home', name='home'),

    url(r'^create-sales-person/$','inventoryapp.views.create_sales_person', name='create_person_url'),
    url(r'^make-transaction$','inventoryapp.views.create_transactions', name='create_transactions_url'),
    url(r'^add-customer$','inventoryapp.views.add_customer', name='add_customer_url'),
    url(r'^add-product$','inventoryapp.views.add_product', name='add_product_url'),
       url(r'^login/$',login,{'template_name':'login.html'}, name='login_url'),
    url(r'^logout/$',logout, {'next_page': '/login/'},name='logout_url'),
    url(r'^admin/', include(admin.site.urls)),
)
