from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    tittle = "Django Course!!"
    return render(request, 'index.html', {
        'tittle': tittle
    })

def about(request):
    return render(request, 'about.html')

def projects(request):
    # projects = list(Project.objects.values())
    projects = list(Project.objects.all())
    # return JsonResponse(projects, safe=False)
    return render(request, 'projects.html', {
        'projects': projects
    })

def tasks(request):
    # task = Task.objects.get(id=id)
    # task = get_object_or_404(Task, id=id)
    # return HttpResponse('Task: %s' % task.title)
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {
        'tasks': tasks
    })