from django.db import models


class Project(models.Model):
    project_name = models.CharField(max_length=540)
    Project_Discription = models.TextField()
    images = models.ImageField(upload_to = 'Projects')

    def __str__(self):
        return self.project_name
        
