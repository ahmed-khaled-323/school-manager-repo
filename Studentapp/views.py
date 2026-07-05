from django.shortcuts import render,redirect
from accountmanager.models import  User, Studentprofile
from .models import Grades
from django.contrib.auth import logout
from django.contrib import messages
from Teacherapp.models import Weeklyschedule

# Create your views here.
def GetGrades(student_id,Month="1"):
        print(Month)
        get_Grades = Grades.objects.filter(Month = Month,student = student_id)
        return get_Grades
def GetWeeklyschedule(AcademicYear,classes):
      Get_Weekly_schedule = Weeklyschedule.objects.filter(Academicyear =AcademicYear ,classes =classes)
      
      return Get_Weekly_schedule 


def dashboard(request):
    
    if request.user.is_authenticated:
        get_Grades = None
        Get_Weekly_schedule = None
        Username = request.user.username
        try:
            student = Studentprofile.objects.get(name__username = Username)
            Get_Weekly_schedule =GetWeeklyschedule(student.AcademicYear , student.klass)
            if Get_Weekly_schedule:
                print(Get_Weekly_schedule)
            else:print("none")

            if request.method == "POST":
                Month = request.POST.get("Month")
                if GetGrades(student.id , Month):
                     get_Grades=GetGrades(student.id , Month)
                else:messages.error(request,'its Month does not exist retern to school')

            
        except Exception as e:
             print(e)
             return redirect("logout")
        
        context = {'username' : Username , "Grades" : get_Grades,"Weekly_schedule":Get_Weekly_schedule}

    
    return render (request,'student_dashboard.html',context)



