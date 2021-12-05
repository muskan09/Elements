from django.db import models

# Create your models here.
class AboutStuff(models.Model):
    title = models.CharField(max_length=100)
    info_para = models.TextField(blank=True)
    img = models.ImageField(upload_to='dp/', blank=True)

    def __str__(self):
        return self.title

class WorkExp(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='workexp/', blank=True)
    start_date = models.DateTimeField(blank=True)
    end_date = models.DateTimeField(blank=True)
    more = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Education(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='workexp/', blank=True)
    start_date = models.DateTimeField(blank=True)
    end_date = models.DateTimeField(blank=True)
    more = models.TextField(blank=True) 

    def __str__(self):
        return self.title

class Language(models.Model):
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, blank=True)
    color = models.CharField(max_length=30, default='white')

    def __str__(self):
        return self.title

class Domain(models.Model):
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, blank=True)
    color = models.CharField(max_length=30, default='white')


    def __str__(self):
        return self.title

class Platform(models.Model):
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, blank=True)
    color = models.CharField(max_length=30, default='white')

    def __str__(self):
        return self.title

    