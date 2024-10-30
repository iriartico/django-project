from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)

    # Con este cambio nos mostrará los nombres y no Object
    def __str__(self):
        # return super().__str__()
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    
    # Con este cambio nos mostrará los nombres y no Object
    def __str__(self):
        # return super().__str__()
        return self.title + ' -- Project: ' + self.project.name
 