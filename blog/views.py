from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Blog


def all_articles(request):
    contact_list = Blog.objects.all()
    paginator = Paginator(contact_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/articles.html', {'page_obj': page_obj})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/article_detail.html', {'blog': blog})
