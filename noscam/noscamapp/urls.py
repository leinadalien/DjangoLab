from django.urls import path
from .views import *

urlpatterns = [
    path('', NoScamHome.as_view(), name='home'),

]