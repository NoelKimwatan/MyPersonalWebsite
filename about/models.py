from django.db import models

class About(models.Model):
    my_image = models.ImageField(upload_to='uploads/images/mainpage/about')
    description = models.TextField()


