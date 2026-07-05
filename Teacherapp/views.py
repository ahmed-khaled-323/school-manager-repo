from django.shortcuts import render

# Create your views here.
def dashboard(request):
    username = request.user.username
    context = {'username':username}
    return render(request,'teacher_dashboard.html',context)