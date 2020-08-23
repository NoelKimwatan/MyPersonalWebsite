from django.contrib import admin
from .models import Project


@admin.register(Project)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ["title","tag1","tag2","tag3"]