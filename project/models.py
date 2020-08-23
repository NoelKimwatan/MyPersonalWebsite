from django.db import models



class Project(models.Model):
    
    tag_options = [("machinelearning","machinelearning"),("webdevelopment","webdevelopment"),("electronics","electronics")]

    image = models.ImageField(upload_to="uploads/images/mainpage/projects")
    title = models.CharField(max_length=100)
    github = models.URLField(max_length=300,blank=True)
    live_link = models.URLField(max_length=300,blank=True)
    description = models.TextField()
    tag1 = models.CharField(max_length=50,choices = tag_options)
    tag2 = models.CharField(max_length=50,choices = tag_options,blank=True)
    tag3 = models.CharField(max_length=50,choices = tag_options,blank=True)

