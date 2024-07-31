from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Loan
from .forms import LoanForm

class LoanListCreateView(ListView, CreateView):
    model = Loan
    form_class = LoanForm
    template_name = 'loans/loan_list.html'
    
    def get_queryset(self):
        return Loan.objects.all()

class LoanDetailView(DetailView):
    model = Loan
    template_name = 'loans/loan_detail.html'

class LoanUpdateView(UpdateView):
    model = Loan
    form_class = LoanForm
    template_name = 'loans/add_loan.html'

class LoanDeleteView(DeleteView):
    model = Loan
    success_url = '/loans/'
    template_name = 'loans/loan_confirm_delete.html'
