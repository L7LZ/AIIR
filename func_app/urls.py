from django.urls import path
from . import views

urlpatterns = [
    path('<string:text>', views.index)
]