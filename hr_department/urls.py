from django.urls import path
from .views import *

urlpatterns = [
    path('api/create', CreatePersonInformation.as_view())
]
