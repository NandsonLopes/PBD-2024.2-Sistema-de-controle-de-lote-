from django.urls import path
from .views import DevelopmentListView

urlpatterns = [
    path('development/', DevelopmentListView.as_view(), name='development-list'),
]
