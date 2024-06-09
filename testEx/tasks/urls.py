from django.urls import path

from .views import TaskCreationView, TaskListView, TaskInProgressView, TaskDoneView


urlpatterns = [
    path("create/", TaskCreationView.as_view()),
    path("get/", TaskInProgressView.as_view()),
    path("done/", TaskDoneView.as_view()),
    #     path('task/<slug:task_slug>', name='task')
    path("list/", TaskListView.as_view()),
    # path('free_tasks/', TasksInPendingView.as_view()),
]
