from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customers/', include('customers.urls')),
    path('loans/', include('loans.urls')),
    #path('payments/', include('payments.urls')),
    path('payments/', include('payments.urls')),
    #path('', include('home.urls')),
    path('', RedirectView.as_view(url='/admin/', permanent=True)),
]
