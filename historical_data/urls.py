from django.urls import path
from .views import FinanceListView

app_name = 'historical_data'
urlpatterns = [
    # Historical finance data
    path('history/<slug:ticker_slug>', FinanceListView.as_view()),
]