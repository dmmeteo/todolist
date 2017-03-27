from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.tasks_list, name='tasks_list'),
    url(r'^task/change_status/$', views.change_status, name='change_status'),
]