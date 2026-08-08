from django.shortcuts import render,redirect
from users.forms import RegisterForm,login_form,Changepassword,PasswordResetForm,PasswordResetConfirmForm,EditProfileModelForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView,UpdateView

from django.contrib.auth.views import PasswordChangeView,PasswordResetView , PasswordResetConfirmView
from django.urls import reverse_lazy
from django.contrib import messages

from django.contrib.auth import get_user_model
User=get_user_model()


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
    return render(request,'registration/sign_up.html',{'form':form})

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
    return render(request,'registration/sign_in.html',{'form':form})


class Sign_in(LoginView):
    template_name = 'registration/sign_in.html'
    form_class=login_form
    def get_success_url(self):
        next_url=self.request.GET.get('next')
        return next_url if next_url else super().get_success_url()


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



class ProfileView(TemplateView):  
    template_name='account/profile.html'
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        user=self.request.user
        context['username']=user.username
        context['email']=user.email
        context['name']=user.get_full_name()
        context['member_since']=user.date_joined
        context['last_login']=user.last_login
        context['bio']=user.bio
        context['profileimage']=user.profile
        return context


class change_password(PasswordChangeView):
    template_name='account/password_change.html'
    form_class=Changepassword



class PasswordResetView(PasswordResetView):
    template_name='registration/reset_password.html'
    form_class=PasswordResetForm
    success_url = reverse_lazy('sign-in')
    html_email_template_name='registration/reset_email.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["protocol"] = 'https' if self.request.is_secure() else 'http'
        context['domain']=self.request.get_host()
        return context

    def form_valid(self, form):
        messages.success(self.request,'A Reset Email sent. Please Check you Email')
        return super().form_valid(form)
    
    
class PasswordResetConfirmView(PasswordResetConfirmView):
    form_class=PasswordResetConfirmForm
    template_name='registration/reset_password.html'
    success_url = reverse_lazy('sign-in')


    def form_valid(self, form):
        messages.success(self.request,'Password Reset Succesfully')
        return super().form_valid(form)


""" 

class EditProfileView(UpdateView):
    model=User
    form_class=EditProfileModelForm
    template_name='account/update_profile.html'
    context_object_name='form'

    def get_object(self):
        return self.request.user

    def get_form_kwargs(self):
        kwargs=super().get_form_kwargs()
        kwargs['userprofile']=userprofile.objects.get(user=self.request.user)
        return kwargs

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        user_profile=userprofile.objects.get(user=self.request.user)
        context['form']=self.form_class(instance=self.object,userprofile=user_profile)
        return context

    def form_valid(slef,form):
        form.save(commit=True)
        return redirect('profile')


     """
class EditProfileView(UpdateView):
    model=User
    form_class=EditProfileModelForm
    template_name='account/update_profile.html'
    context_object_name='form'

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        form.save()
        return redirect('profile')