from django.shortcuts import render
# Create your views here.

from django.views.generic import TemplateView
from django.views.generic import ListView
from task.models import TaskItem


class Index(TemplateView):
    template_name = "base.html"

class TaskListView(ListView):
    template_name = "taskitem_list.html"
    queryset = TaskItem.objects.all()