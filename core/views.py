from django.shortcuts import render

from core.models import Company

def company_list(request):
    companies = Company.objects.all()
    context = {
        'companies': companies
    }
    return render(request, 'core/company_list.html', context)
# Create your views here.
