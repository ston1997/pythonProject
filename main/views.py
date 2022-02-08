from django.shortcuts import render, redirect
from .models import task
from .forms import TaskForm

def index(request):
    tasks=task.objects.all()
    return render(request, 'main/index.html', {'title': 'главная стрица сайта', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def login(request):
    return render(request, 'main/login.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error ='форма была неверной'
    form=TaskForm
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)