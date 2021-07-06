from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,  DetailView, CreateView, DeleteView, UpdateView
from .models import TodoModel
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

import sys
import pathlib
# base.pyのあるディレクトリの絶対パスを取得
current_dir = pathlib.Path(__file__).resolve().parent
# モジュールのあるパスを追加
sys.path.append( str(current_dir) + '/../' )

from ml_models import classify
 
# Create your views here.
def todo(request):
  return HttpResponse('')


 
# Create your views here.
 
class TodoList(ListView):
    template_name = 'list.html'
    model = TodoModel # 追記

class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel

class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('list')


    def form_valid(self, form):
        # value_list = self.model.objects.values_list('title')
        # print(form.instance.title)
        # https://stackoverflow.com/questions/51905712/how-to-get-the-value-of-a-django-model-field-object
        # obj = self.model.objects.first()
        # obj = self.model.objects.get(id=1).field
        # field_object = self.model._meta.get_field('title')
        # field_value = getattr(obj, field_object.attname)
       
        category = classify(form.instance.title)

        # https://stackoverflow.com/questions/21652073/django-how-to-set-a-hidden-field-on-a-generic-create-view
        form.instance.category = category
        return super(TodoCreate, self).form_valid(form)


class TodoDelete(DeleteView):
    template_name = 'delete.html'
    model = TodoModel
    success_url = reverse_lazy('list')

class TodoUpdate(UpdateView):
    template_name = 'update.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate', 'category')
    success_url = reverse_lazy('list')