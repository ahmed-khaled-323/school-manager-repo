from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login,logout
from . import models
# Create your views here.



def loginsystem(request):
    if not request.user.is_authenticated:
    
        if request.method == "POST":
        
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request , username = username , password=password)

            if user is not None:
                login(request,user)
                profile = None
                try:
                    profile = models.Studentprofile.objects.get(name__username = username)
                    
                    return redirect("Sdashboard/")
                except: 
                    try:
                        profile = models.Teacherprofile.objects.get(name__username = username)
                        return redirect("tdashboard/")
                    except: print("no profile")
    else: return redirect("Sdashboard/")
    return render (request ,"login.html")

def logoutsystem(request):
    logout(request)
    return redirect("login")



