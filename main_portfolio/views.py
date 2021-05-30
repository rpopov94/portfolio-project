from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Project


def listing(request):
    contact_list = Project.objects.all()
    paginator = Paginator(contact_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main_portfolio/about.html', {'page_obj': page_obj})


# def homePageView(request):
#     projects = Project.objects.all()
#     return render(request, 'main_portfolio/about.html', {'projects': projects})
