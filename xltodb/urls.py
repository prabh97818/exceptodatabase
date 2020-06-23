from django.urls import path
from .views import ParseExcel

urlpatterns = [
    path('', ParseExcel.as_view()),
]