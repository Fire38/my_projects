from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()
    library = models.TextField(default="pass")
    study_project = models.BooleanField()

    def __str__(self):
        return self.title
