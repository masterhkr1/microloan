from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from rest_framework import generics
from .models import Loan
from .forms import LoanForm
from .serializers import LoanSerializer

class LoanListCreateView(generics.ListCreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

class LoanDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

def loan_list(request):
    if request.method == 'GET':
        loans = Loan.objects.all()
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            data = list(loans.values('id', 'customer', 'amount', 'interest_rate', 'period', 'amortization'))
            return JsonResponse(data, safe=False)
        return render(request, 'loans/loan_list.html', {'loans': loans})

def loan_detail(request, pk):
    loan = get_object_or_404(Loan, pk=pk)
    return render(request, 'loans/loan_detail.html', {'loan': loan})

def add_loan(request):
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                data = form.instance
                response_data = {
                    'id': data.id,
                    'customer': data.customer,
                    'amount': data.amount,
                    'interest_rate': data.interest_rate,
                    'period': data.period,
                    'amortization': data.amortization,
                }
                return JsonResponse(response_data)
            return redirect('loan_list')
    else:
        form = LoanForm()
    return render(request, 'loans/add_loan.html', {'form': form})
