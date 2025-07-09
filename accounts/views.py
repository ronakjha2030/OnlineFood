from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserForm 
from .models import User
from django.contrib import messages

def registerUser(request):
    if request.method == "POST":
        print(request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            user = form.save(commit=False)
            user.set_password(password)
            user.role = User.CUSTOMER
            form.save()
            messages.success(request,'YOU HAVE BEEN REGISTERED SUCCESSFULLY.....')
            return redirect('registerUser')
        else:
            print(form.errors)
            context = {'form': form}
            return render(request, 'accounts/registerUser.html', context)
    else: 
        form = UserForm()
        context ={
            'form': form
        }
        return render(request,'accounts/registerUser.html',context)