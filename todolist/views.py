from django.shortcuts import redirect
from datetime import datetime
from annoying.decorators import render_to
from .forms import CreateTask
from couchdbcurl.client import Document
import django_couch


# Create your views here.
@render_to('home.html')
def tasks_list(request):
    title = 'Home'
    tasks = request.db.view('tasks/active').rows
    form = CreateTask(request.POST or None)

    if request.POST and form.is_valid():
        data = form.cleaned_data
        now = datetime.now()

        doc = Document(_db=request.db, type='task')
        doc.update(data)
        doc['created'] = now.isoformat()
        doc['status'] = 'active'
        task_id = 'task_%s' % now.strftime("%d_%m_%Y_%H_%M_%S")

        doc.create(task_id)
        return redirect('/')

    return {'title': title, 'tasks': tasks, 'form': form}

