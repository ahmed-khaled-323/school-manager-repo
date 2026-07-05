from django.db import models
import uuid
from accountmanager.models import Studentprofile

# Create your models here.

class Subject(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField()
    def __str__(self):
        return self.name
    

class Grades(models.Model):
    student = models.ForeignKey(Studentprofile,on_delete=models.DO_NOTHING)
    Month = models.CharField(max_length=10,choices=(('1','frist'),('2','secound'),('3','threrd')))
    Subjectid = models.OneToOneField(Subject,on_delete=models.DO_NOTHING)
    Grade = models.IntegerField()
    Evaluation = models.CharField(max_length=20,choices=(('ممتاز','excellent'),('مقبول','acceptable'),('صاقط','fall')))


