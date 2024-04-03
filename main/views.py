from django.shortcuts import render

from .models import Post, Hottest

def home_page(request):
    context = {
        'posts': Post.objects.all(),
        'hottest': Hottest.objects.all()
    }
    return render(request, 'main/home_page.html', context)

def article(request, id):
    context = {
        'post': Post.objects.get(id=id)
    }
    return render(request, 'main/article.html', context)

def hottest(request, id):
    context = {
        'hot': Hottest.objects.get(id=id)
    }
    return render(request, 'main/hot.html', context)

def images(request):
    return render(request, 'main/images.html')