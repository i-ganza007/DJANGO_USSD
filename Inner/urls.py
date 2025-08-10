from django.urls import path
from Inner.views import ussd_endpoint

urlpatterns = [
    path('ussd_endpoint/',ussd_endpoint,name='ussd_test')
]