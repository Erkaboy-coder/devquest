from django.urls import path
from .views import ChallengeListCreateView

urlpatterns = [
    path('challenges/', ChallengeListCreateView.as_view(), name='challenge-list'),
]
