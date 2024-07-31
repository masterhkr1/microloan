from django.urls import path
from .views import LoanListCreateView, LoanDetailView, LoanUpdateView, LoanDeleteView

urlpatterns = [
    path('', LoanListCreateView.as_view(), name='loan-list'),
    path('add/', LoanListCreateView.as_view(), name='loan-create'),
    path('<int:pk>/', LoanDetailView.as_view(), name='loan-detail'),
    path('<int:pk>/edit/', LoanUpdateView.as_view(), name='loan-update'),
    path('<int:pk>/delete/', LoanDeleteView.as_view(), name='loan-delete'),
]
