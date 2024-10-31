from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import render, get_object_or_404
from .forms import CreateNewTask

# Create your views here.
def index(request):
    title = "Django Course"
    return render(request, 'index.html', {
        'title': title
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

def create_task(request):
    # print(request.GET['title'])
    # print(request.GET['description'])
    # Task.objects.create(title=request.GET['title'], description=request.GET['description'],
    #                     projectkey=1)
    # return render(request, 'create_task.html',{
    #     'form': CreateNewTask()
    # })
    # if request.method == 'GET':Dreturn render(request, 'create_task.html',{
    #     'form': CreateNewTask()
    pass