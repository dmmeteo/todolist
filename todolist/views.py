from django.shortcuts import redirect
from django.http import HttpResponse, Http404
from datetime import datetime
from annoying.decorators import render_to
from .forms import CreateTask
from couchdbcurl.client import Document
import django_couch


# Create your views here.
@render_to('home.html')
def tasks_list(request):
    tasks = request.db.view('tasks/all_tasks').rows
    form = CreateTask(request.POST or None)

    if request.POST and form.is_valid():
        data = form.cleaned_data
        now = datetime.now()
        doc = Document(_db=request.db, type='task')
        task_id = 'task_%s' % now.strftime("%d_%m_%Y_%H_%M_%S")

        doc.update(data)
        doc['created'] = now.isoformat()
        doc['status'] = 'active'
        doc.create(task_id)
        return redirect('/')

    return {'tasks': tasks, 'form': form}


def change_status(request):
    if request.GET:
        try:
            doc = request.db[request.GET['task_id']]
            if doc['status'] == 'active':
                doc['status'] = 'completed'
            elif doc['status'] == 'completed':
                doc['status'] = 'active'
            doc.save()
        except django_couch.ResourceNotFound:
            raise Http404
        print doc

        return HttpResponse('ok', content_type='text/html')
    else:
        return HttpResponse('no', content_type='text/html')
