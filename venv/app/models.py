from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    faculty = models.CharField(max_length=50)
    registration_date = models.CharField(max_length=50)

    def __str__(self) ->str:
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=50)
    joined_at = models.DateField(auto_now=True,  )


    def __str__(self) -> str :
        return self.name
