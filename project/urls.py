from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from trades import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', views.ViewTrades.as_view(), name="viewtrades"),
    path('createtrade/', views.CreateTrade.as_view(), name="createtrade"),
    path('updatetrade/<int:pk>', views.UpdateTrade.as_view(), name="updatetrade"),
    path('deletetrade/<int:pk>/', views.DeleteTrade.as_view(), name="deletetrade"),
]
