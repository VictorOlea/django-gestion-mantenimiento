from django.urls import path
from .views import list_tasks, create_task, delete_task, aprove_task, summary_tasks

urlpatterns = [
    path('', list_tasks),
    path('new/', create_task, name='create_task'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'),
    path('aprove_task/<int:task_id>/', aprove_task, name='aprove_task'),
    path('summary/', summary_tasks, name='summary_task')
]
