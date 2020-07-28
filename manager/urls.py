from django.urls import path

from . import views

app_name = 'manager'

urlpatterns = [
    path('', views.manager, name='manager'),
    path('deactivate/', views.deactivate, name='deactivate'),
    path('deactivate/account/', views.deactivate_account, name='deactivate_confirm'),
]