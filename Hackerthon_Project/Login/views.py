from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def login(request):
    if request.method ==  "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, 'login.html', {'error': '아이디 또는 패스워드가 틀립니다.'})
    return render(request,"login/login.html")

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('main')
    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(

                username=request.POST["username"],password=request.POST["password1"])
            auth.login(request,user)
            return redirect('main')    
        return render(request, 'signup.html')



            
    

