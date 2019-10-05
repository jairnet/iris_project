from django.urls import path, re_path
# from . import views
from .views import AddressingDateView

# app_name = 'jtest'

urlpatterns = [
    path('date/', AddressingDateView.as_view(), name='addressing-date'),
    # re_path(r'^fecha/(?P<year>[0-9]{4})-(?P<month>[0-9]{2})-(?P<day>[0-9]{2})/$', views.addressing_date, name='addressing-date')
]