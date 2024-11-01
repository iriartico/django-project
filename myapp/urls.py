from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("about/", views.about),
    # path('hello/<str:username>', views.hello),
    path("projects/", views.projects, name="projects"),
    path("projects/<int:id>", views.project_detail, name="project_detail"),
    path("create-project/", views.create_project, name="create_project"),
    path("tasks/", views.tasks, name="view_tasks"),
    path("create-task/", views.create_task, name="create_task"),
]
