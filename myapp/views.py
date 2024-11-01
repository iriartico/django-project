from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewProject, CreateNewTask


# Create your views here.
def index(request):
    title = "Django Course"
    return render(request, "index.html", {"title": title})


def about(request):
    return render(request, "about.html")


def projects(request):
    # projects = list(Project.objects.values())
    projects = list(Project.objects.all())
    # return JsonResponse(projects, safe=False)
    return render(request, "projects.html", {"projects": projects})


def create_project(request):
    if request.method == "GET":
        return render(request, "create_project.html", {"form": CreateNewProject()})
    else:
        Project.objects.create(
            name=request.POST["name"],
        )
        # return redirect("tasks/")
        return redirect("projects")


def tasks(request):
    # task = Task.objects.get(id=id)
    # task = get_object_or_404(Task, id=id)
    # return HttpResponse('Task: %s' % task.title)
    tasks = Task.objects.all()
    return render(request, "tasks.html", {"tasks": tasks})


def create_task(request):
    if request.method == "GET":
        return render(request, "create_task.html", {"form": CreateNewTask()})
    else:
        Task.objects.create(
            title=request.POST["title"],
            description=request.POST["description"],
            project_id=2,
        )
        # return redirect("tasks/")
        return redirect("view_tasks")


def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    # tasks = Task.objects.all()
    return render(request, "project/detail.html", {"project": project, "tasks": tasks})
