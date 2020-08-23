from django.db import models

class Experience(models.Model):
    start_date = models.DateField()
    end_date = models.DateField(blank=True,null=True)
    title = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return (self.title)

class Education(models.Model):
    start_date = models.DateField()
    end_date = models.DateField(blank=True,null=True)
    title = models.CharField(max_length=100)
    certificate = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return (self.title)

class Certification(models.Model):
    date_earned = models.DateField()
    title = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    certificate_link = models.URLField(max_length=300,blank=True,null=True)
    description = models.TextField()

    def __str__(self):
        return (self.title)

class Resume(models.Model):
    file = models.FileField(upload_to="uploads/files/resume")

