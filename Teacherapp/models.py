from django.db import models
from accountmanager.models import Teacherprofile,School_classes,Academic_year


# Create your models here.
class Week(models.Model):
    day_name = models.CharField()
    date = models.DateField()
    
    def __str__(self):
        return self.day_name

class Session(models.Model):
    session =  models.CharField(max_length=1)
    def __str__(self):
        return self.session



class Weeklyschedule(models.Model):    
    Teacher_name =models.ForeignKey(Teacherprofile ,on_delete=models.DO_NOTHING)
    day = models.ForeignKey(Week,on_delete=models.DO_NOTHING)
    Academicyear = models.ForeignKey(Academic_year , on_delete=models.DO_NOTHING)
    classes = models.ForeignKey(School_classes , on_delete=models.DO_NOTHING)
    session =  models.OneToOneField(Session,on_delete=models.DO_NOTHING)







