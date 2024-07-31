from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Payment
from .forms import PaymentForm

class PaymentListCreateView(ListView, CreateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'payments/payment_list.html'
    
    def get_queryset(self):
        return Payment.objects.all()

class PaymentDetailView(DetailView):
    model = Payment
    template_name = 'payments/payment_detail.html'

class PaymentUpdateView(UpdateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'payments/add_payment.html'

class PaymentDeleteView(DeleteView):
    model = Payment
    success_url = '/payments/'
    template_name = 'payments/payment_confirm_delete.html'
