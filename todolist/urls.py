from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.tasks_list, name='home'),
    url(r'^tasks/([^/]+)/$', views.tasks_by_status, name='tasks_by_status'),
    url(r'^task/change_status/$', views.change_status, name='change_status'),
]