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
    items_left = len(request.db.view('tasks/by_status', key='active').rows)
    items_completed = request.db.view('tasks/by_status', key='completed').rows
    form = CreateTask(request.POST or None)

    if request.POST and form.is_valid():
        data = form.cleaned_data
        now = datetime.now()
        task_id = 'task_%s' % now.strftime("%d_%m_%Y_%H_%M_%S")
        doc = Document(_db=request.db, type='task')

        doc.update(data)
        doc['created'] = now.isoformat()
        doc['status'] = 'active'
        doc.create(task_id)
        return redirect('/')

    return {
        'tasks': tasks,
        'form': form,
        'items_left': items_left,
        'items_completed': items_completed,
    }


@render_to('tasks_by_status.html')
def tasks_by_status(request, status):
    title = status.title()
    tasks = request.db.view('tasks/by_status', key=status).rows
    items_left = len(request.db.view('tasks/by_status', key='active').rows)
    items_completed = request.db.view('tasks/by_status', key='completed').rows
    return {
        'tasks': tasks,
        'title': title,
        'items_left': items_left,
        'items_completed': items_completed,
    }


def change_status(request):
    if request.GET:
        try:
            doc = request.db[request.GET['task_id']]
            doc['status'] = request.GET['task_status']
            doc.save()
        except django_couch.ResourceNotFound:
            raise Http404

        return HttpResponse('ok', content_type='text/html')
    else:
        return HttpResponse('no', content_type='text/html')


def clear_items(request):
    docs = request.db.view('tasks/by_status', key='completed').rows
    for doc in docs:
        try:
            doc = request.db[doc.id]
            doc['status'] = 'closed'
            doc.save()
        except django_couch.ResourceNotFound:
            raise Http404
    return redirect(request.META.get('HTTP_REFERER', '/'))