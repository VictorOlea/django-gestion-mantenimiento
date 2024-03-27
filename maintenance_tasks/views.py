from django.shortcuts import render, redirect
from .models import Maintenance_Tasks

# Create your views here.
def list_tasks(request):
    tasks = Maintenance_Tasks.objects.all()
    return render(request, 'list_tasks.html', {"tasks": tasks})

def create_task(request):
    task = Maintenance_Tasks(title=request.POST['title'], description=request.POST['description'], responsible=request.POST['responsible'])
    task.save()
    return redirect('/tasks/')

def delete_task(request, task_id):
    delete_task = Maintenance_Tasks.objects.get(id=task_id)
    delete_task.delete()
    return redirect('/tasks/')

def aprove_task(request, task_id):
    aprove_task = Maintenance_Tasks.objects.get(id=task_id)
    aprove_task.status = "Aprobada"
    aprove_task.save(update_fields=['status'])
    return redirect('/tasks/')

def summary_tasks(request):
    tasks = Maintenance_Tasks.objects.all()
    return render(request, 'summary.html', {"tasks": tasks})