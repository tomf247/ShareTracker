from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from trades import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', views.ViewTrades.as_view(), name="viewtrades"),
]
