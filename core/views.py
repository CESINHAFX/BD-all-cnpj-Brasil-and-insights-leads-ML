from django.shortcuts import render

from core.models import Company

def company_list(request):
    from django.core.paginator import Paginator
    query = request.GET.get('q', '')
    company_list = Company.objects.filter(city__icontains=query)
    paginator = Paginator(company_list, 100)
    page_number = request.GET.get('page')
    companies = paginator.get_page(page_number)
    context = {
        'companies': companies
    }
    return render(request, 'core/company_list.html', context)
# Create your views here.
