# documents/models.py

from django.db import models


class Business(models.Model):
    name = models.CharField(max_length=255)
    Description = models.TextField()

    def __str__(self):
        return self.name


class SubBusiness(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(Business, related_name='sub_businesses', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Folder(models.Model):
    name = models.CharField(max_length=255)
    business = models.ForeignKey(Business, related_name='folders', on_delete=models.CASCADE, null=True, blank=True)
    sub_business = models.ForeignKey(SubBusiness, related_name='folders', on_delete=models.CASCADE, null=True,
                                     blank=True)
    parent_folder = models.ForeignKey('self', related_name='sub_folders', on_delete=models.CASCADE, null=True,
                                      blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class File(models.Model):
    name = models.CharField(max_length=255)
    folder = models.ForeignKey(Folder, related_name='files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
