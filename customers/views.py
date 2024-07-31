from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Customer
from .forms import CustomerForm

def customer_list(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            data = list(customers.values('id', 'name', 'email', 'phone'))
            return JsonResponse(data, safe=False)
        return render(request, 'customers/customer_list.html', {'customers': customers})

def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'customers/customer_detail.html', {'customer': customer})

def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                data = form.instance
                response_data = {
                    'id': data.id,
                    'name': data.name,
                    'email': data.email,
                    'phone': data.phone,
                }
                return JsonResponse(response_data)
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'customers/add_customer.html', {'form': form})
