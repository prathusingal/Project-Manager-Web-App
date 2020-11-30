from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from account.models import userprofile,project

class UserProfileForm(ModelForm):
    class Meta:
        model=userprofile
        fields=['full_name','employee_id','gender','DOB','email','mobile_number','profile_pic']

class Boss_details_Form(ModelForm):
    class Meta:
        model=project
        fields = ['boss_name','boss_email','boss_mobile_number']

class Project_details_Form(ModelForm):
    class Meta:
        model=project
        fields = ['project_title','deadline','project_description','resources']

class Employee_details_Form(ModelForm):
    class Meta:
        model=project
        fields = ['employee_id','employee_name']
