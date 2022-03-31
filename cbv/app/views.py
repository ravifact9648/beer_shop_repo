from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, DeleteView,UpdateView
from django.urls import reverse_lazy

from app.models import Beer
def index(request):
    return render(request,'app/index.html')

class Create(CreateView):
    model=Beer
    fields=('name','taste','color','price')
    template_name='app/create.html'
    success_url=reverse_lazy('index')

class List(ListView):
    model=Beer
    template_name='app/list.html'
    context_object_name='list'
    

class Detail(DetailView):
    model=Beer
    template_name='app/detail.html'
    context_object_name='beer'

class Delete(DeleteView):
    model=Beer
    context_object_name='delete'
    # template_name='delete.html'
    success_url=reverse_lazy('index')

class Update(UpdateView):
    model=Beer
    fields=['taste','color','price']
    template_name='app/create.html'
    success_url='/list'


