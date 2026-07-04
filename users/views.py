from django.shortcuts import render,redirect
from users.forms import RegisterForm,login_form
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.http import HttpResponse

def sign_up(request):
    form=RegisterForm()
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            password=form.cleaned_data.get('password1')
            user.set_password(password)
            user.is_active=False
            user.save()
            return redirect('sign-in')
    return render(request,'sign_up.html',{'form':form})

# def sign_in(request):
#     if request.method=='POST':
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#         user=authenticate(username=username,password=password)

#         if user is not None:
#             login(request,user)
#             return redirect('dashboard')
#         else:
#             return render(request,'sign_in.html',{'error':'Invalid Username or Password'})
        
#     return render(request,'sign_in.html')

def sign_in(request):
    form=login_form()
    if request.method=='POST':
        form=login_form(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('dashboard')
    return render(request,'sign_in.html',{'form':form})

def sign_out(request):
    if request.method=='POST':
        logout(request)
    
    return redirect('dashboard')


def active_user(request,id,token):
    try:
        user=User.objects.get(id=id)
        if default_token_generator.check_token(user,token):
            user.is_active=True
            user.save()
            return  redirect('sign-in')
        else:
            return  HttpResponse('Invalid id or Token')
    except User.DoesNotExist:
        return HttpResponse('User Not Found')


def admin_dashboard(request):
    return render(request,'admin/admin_dashboard.html')