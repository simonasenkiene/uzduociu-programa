from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Task

from django.shortcuts import render
from .models import Task
from django.contrib.auth.decorators import login_required

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'uzduotys/task_list.html', {'tasks': tasks})