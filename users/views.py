from django.shortcuts import render,redirect
from users.forms import RegisterForm

def sign_up(request):
    form=RegisterForm()
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            password=form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            return redirect('sign-in')
    return render(request,'sign_up.html',{'form':form})