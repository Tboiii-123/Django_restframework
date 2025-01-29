from django.db import models

# Create your models here.


class Student(models.Model):

    name = models.CharField(max_length=200)
    age =models.IntegerField()
    description = models.TextField()

    date_enrollled = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    





class Document(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')  # For general file upload
    uploaded_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):

        return self.title
    