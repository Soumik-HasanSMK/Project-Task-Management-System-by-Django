from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from datetime import date


def task_list(request):
    query = request.GET.get('search', '')
    today = date.today()


    if query:
        tasks = Task.objects.filter(
            title__icontains=query
        ) | Task.objects.filter(
            description__icontains=query
        )
    else:
        tasks = Task.objects.all()


    overdue_tasks = tasks.filter(deadline__lt=today, status__iexact="Pending")


    return render(request, 'tasks/task_list.html', {
        'tasks': tasks,
        'query': query,
        'today': today,
        'overdue_tasks': overdue_tasks.exists(),
    })




# Create Task
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})


# Update Task
def update_task(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/update_task.html', {'form': form, 'task': task})


# Delete Task
def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == "POST":
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/delete_task.html', {'task': task})


