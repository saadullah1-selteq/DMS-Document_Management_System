# documents/admin.py

from django.contrib import admin
from .models import Business, SubBusiness, Folder, File

@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    pass

@admin.register(SubBusiness)
class SubBusinessAdmin(admin.ModelAdmin):
    pass

@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    pass

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    pass
