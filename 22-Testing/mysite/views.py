from django.shortcuts import render

from mysite.models import Blog


def home(request):
    blog = Blog.objects.get(pk=1)
    return render(request,
                  'mysite/index.html',
                  {'title': 'Hello',
                   'blog': blog})
