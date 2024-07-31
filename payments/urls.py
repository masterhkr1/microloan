from django.urls import path
from .views import PaymentListCreateView, PaymentDetailView, PaymentUpdateView, PaymentDeleteView

urlpatterns = [
    path('', PaymentListCreateView.as_view(), name='payment-list'),
    path('add/', PaymentListCreateView.as_view(), name='payment-create'),
    path('<int:pk>/', PaymentDetailView.as_view(), name='payment-detail'),
    path('<int:pk>/edit/', PaymentUpdateView.as_view(), name='payment-update'),
    path('<int:pk>/delete/', PaymentDeleteView.as_view(), name='payment-delete'),
]
