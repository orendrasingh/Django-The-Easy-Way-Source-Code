from django.shortcuts import render, get_object_or_404
from django.shortcuts import render

from myapp.models import Flower

from django.http import HttpResponseRedirect
from .forms import MyForm

from django.contrib.auth.decorators import permission_required

def index(request):

    # flowers = Flower.objects.all()

    q = request.GET.get('q', None)
    if q is None or q is "":
        flowers = Flower.objects.all()
    elif q is not None:
        flowers = Flower.objects.filter(title__contains=q)
    
    return render(request, 'myapp/index.html', {'flowers': flowers })

def detail(request, slug=None):

    flower = get_object_or_404(Flower, slug=slug)

    return render(request, 'myapp/detail.html', {'flower': flower})

def tags(request, slug=None):
    
    flowers = Flower.objects.filter(tags__slug=slug)
    
    return render(request, 'myapp/index.html', {'flowers': flowers })

@permission_required('myapp.add_flower', raise_exception=True)
def create(request):
    if request.method == 'POST':
        form = MyForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = MyForm()
    return render(request, 'myapp/create.html', {'form': form})

@permission_required('myapp.change_flower', raise_exception=True)
def edit(request, pk=None):
    flower = get_object_or_404(Flower, pk=pk)
    if request.method == "POST":
        form = MyForm(request.POST, request.FILES or None, instance=flower)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = MyForm(instance=flower)
        
    return render(request, 'myapp/edit.html', {'form': form, 'pk': pk})

@permission_required('myapp.change_delete', raise_exception=True)
def delete(request, pk=None):
    flower = get_object_or_404(Flower, pk=pk)
    delete = request.GET.get('delete', None)
    if delete == 'yes':
        flower.delete()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'myapp/confirm.html',
                      {'flower': flower})
