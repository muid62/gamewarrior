from django.shortcuts import render
from blog.models import Category, Blog


# Create your views here.
def blog(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs,

    }
    return render(request, 'blog/categories.html', context)
