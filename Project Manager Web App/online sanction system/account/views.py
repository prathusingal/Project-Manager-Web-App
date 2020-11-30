from django.shortcuts import get_object_or_404
from datetime import datetime
from django import forms
from account.forms import ( UserProfileForm,Boss_details_Form,Project_details_Form,Employee_details_Form
                            )
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from . import models
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .models import userprofile,project
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.db.models import F
from django.core.mail import EmailMessage,send_mail

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return render(request,'accounts/login.html',{})
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password_form.html', {
        'form': form
    })


def my_view(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        USER = authenticate(username=username, password=password)

        if USER:
            id=models.userprofile.objects.get(user__username=request.POST.get('username'))
            login(request, USER)
            if id.role=='Boss':
                return HttpResponseRedirect('/Boss/homepage/')
            elif id.role=='Employee':
                return HttpResponseRedirect('/Employee/homepage/')
            else:
                return HttpResponseRedirect('/admin/')
        else:
            messages.error(request, 'You entered wrong password or username!')
            return render(request,"accounts/login.html",{})

    else:
        return render(request,"accounts/login.html",{})



def Boss_homepage(request):
    return render(request,"Boss/homepage.html",{})


def Boss_view_profile(request):
    return render(request, 'Boss/showProfile.html', {})


def Boss_edit_profile(request):
    instance=request.user.userprofile
    form= UserProfileForm(instance=instance)
    if request.method == 'POST' :
        form = UserProfileForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            instance=request.user.userprofile
            instance=form.save(commit=False)
            instance.save()
            return HttpResponseRedirect('/Student/homepage/')
    context={'form':form}
    return render(request, "Boss/editprofile.html", context)

def Employee_homepage(request):
    return render(request,"Employee/homepage.html",{})

def Employee_view_profile(request):
    return render(request, 'Employee/showProfile.html', {})

def Employee_edit_profile(request):
    instance=request.user.userprofile
    form= UserProfileForm(instance=instance)
    if request.method == 'POST' :
        form = UserProfileForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            instance=request.user.userprofile
            instance=form.save(commit=False)
            instance.save()
            return HttpResponseRedirect('/Student/homepage/')
    context={'form':form}
    return render(request, "Boss/editprofile.html", context)

def user_logout(request):
    logout(request)
    return render(request,'accounts/login.html',{})

#lab
def HOD_Lab_List(request):
    title= 'list of Lab requests'
    queryset=labs.objects.all()
    context={
        "title":title,
        "queryset": queryset,
    }
    return render(request,"HOD/LAB_List.html",context)

def assign_project(request):
    form1 = Boss_details_Form()
    form2 = Employee_details_Form()
    form3 = Project_details_Form()
    if request.method == "POST":
        instance=project.objects.create()
        form1 = Boss_details_Form(request.POST, request.FILES,instance=instance)
        form2=Employee_details_Form(request.POST, request.FILES,instance=instance)
        form3=Project_details_Form(request.POST, request.FILES,instance=instance)
        if form1.is_valid() and form2.is_valid() and form3.is_valid():
            form1.save()
            form2.save()
            instance=form2.save(commit=False)
            instance.filed_by=request.user.id
            instance.progress='in-progress'
            instance.save()
            return Boss_homepage(request)
        else:
            instance.delete()
    return render(request,'Boss/assign_project.html',{'form1':form1,'form2':form2,'form3':form3})

def review_projects(request):
        print("hello")

def project_list(request):
    print("hello")

def project_submit(request):
    print("hello")
