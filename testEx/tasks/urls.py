from django.urls import path


urlpatterns = [

    path('task/create', ),
    path('task/update', ),
    path('tasks/list', ),
    path('task/<slug:task_slug>', name='task')
]