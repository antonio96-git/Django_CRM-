from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('customer/<int:pk>', views.customer_view, name='customer'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('update_customer/<int:pk>', views.update_customer, name='update_customer'),

]