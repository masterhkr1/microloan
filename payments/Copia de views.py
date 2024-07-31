from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.urls import reverse_lazy
from rest_framework import generics
from .models import Payment
from .forms import PaymentForm
from .serializers import PaymentSerializer
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class PaymentCreateView(CreateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'payments/payment_form.html'
    success_url = reverse_lazy('payment-list')  # Redirige a la vista de lista de pagos después de la creación

class PaymentUpdateView(UpdateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'payments/payment_form.html'
    success_url = reverse_lazy('payment-list')
    
class PaymentListCreateView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    
class PaymentDeleteView(DeleteView):
    model = Payment
    template_name = 'payments/payment_confirm_delete.html'
    success_url = reverse_lazy('payment-list')

def payment_list(request):
    if request.method == 'GET':
        payments = Payment.objects.all()
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            data = list(payments.values('id', 'loan', 'amount', 'date'))
            return JsonResponse(data, safe=False)
        return render(request, 'payments/payment_list.html', {'payments': payments})

def payment_detail(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    return render(request, 'payments/payment_detail.html', {'payment': payment})

def add_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                data = form.instance
                response_data = {
                    'id': data.id,
                    'loan': data.loan,
                    'amount': data.amount,
                    'date': data.date,
                }
                return JsonResponse(response_data)
            return redirect('payment_list')
    else:
        form = PaymentForm()
    return render(request, 'payments/add_payment.html', {'form': form})
