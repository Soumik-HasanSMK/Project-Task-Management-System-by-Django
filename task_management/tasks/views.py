from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.contrib.auth import logout

@login_required
def task_list(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login if user is not authenticated
    tasks = Task.objects.filter(user=request.user)  # Only tasks for this user
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})


@login_required
def task_create(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Assign the task to the logged-in user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)  # Restrict to the owner's task
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task_list')

def user_logout(request):
    """Logs out the user and redirects them to the login page."""
    logout(request)  # Clears the session and logs out the user
    return redirect('login') 

def task_search(request):
    query = request.GET.get('q', '')
    if query:
        tasks = Task.objects.filter(title__icontains=query) | Task.objects.filter(description__icontains=query)
    else:
        tasks = Task.objects.all()
    
    return render(request, 'tasks/task_search.html', {'tasks': tasks})