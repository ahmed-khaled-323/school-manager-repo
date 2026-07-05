from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
role = [
    ("student","student"),
    ("teacher","teacher")
]

class Teacherprofile(models.Model):
    id=models.UUIDField(primary_key=True , default= uuid.uuid4, editable= False)
    name = models.OneToOneField(User,on_delete=models.CASCADE)
    phone= models.CharField(max_length=11)
    national_number = models.CharField(max_length=16)
    career = models.CharField(max_length=20)


    def __str__(self):
        return self.name.username


class School_classes(models.Model):
    classes = models.CharField(max_length=3)
    
    def __str__(self):
        return self.classes

class Academic_year(models.Model):
    Academic_year= models.CharField(max_length=2)
    def __str__(self):
        return self.Academic_year

class Studentprofile(models.Model):
    id=models.UUIDField(primary_key=True , default= uuid.uuid4, editable= False)
    name = models.OneToOneField(to=User,on_delete=models.CASCADE)
    AcademicYear= models.OneToOneField(Academic_year, on_delete=models.DO_NOTHING)
    klass = models.OneToOneField(School_classes, on_delete=models.DO_NOTHING)
    student_phone= models.CharField(max_length=11)
    parent_phone= models.CharField(max_length=11)
    national_number = models.CharField(max_length=16)

    def __str__(self):
        return self.name.username
    
