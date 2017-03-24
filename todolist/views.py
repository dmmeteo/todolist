from django.shortcuts import render
from annoying.decorators import render_to
from .forms import CreateTask

# Create your views here.
@render_to('home.html')
def tasks_list(request):
    title = 'Home'
    tasks = [
        {'text': 'lorem1', 'priority': 'alert-info'},
        {'text': 'lorem2', 'priority': 'alert-warning'},
    ]
    form = CreateTask(request.POST or None)
    return {'title': title, 'tasks': tasks, 'form': form}