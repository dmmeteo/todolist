from django.shortcuts import render
from annoying.decorators import render_to


# Create your views here.
@render_to('home.html')
def tasks_list(request):
    title = 'Home'
    hw = 'Hello world!'
    return {'title': title, 'content': hw}