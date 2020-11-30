from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from PIL import Image

class userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50,blank=False)
    profile_pic=models.ImageField(upload_to='profile_pic/',default="profile_pic/statue.jpg",blank=True, null=True)
    full_name = models.CharField(max_length=50,default=None,blank=True, null=True)
    employee_id = models.CharField(max_length=50,default=None,blank=True, null=True)
    GENDER_CHOICES = (
        ('N','------'),
        ('M', 'Male'),
        ('F', 'Female'),
        ('O','Other'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,default=None,blank=False, null=True)
    DOB=models.DateField(default=None,blank=True, null=True,help_text="Use %YYYY-%MM-%DD format.")
    mobile_number=models.CharField(max_length=10,default=None,blank=True, null=True)
    email=models.EmailField(default=None,blank=True, null=True)

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = userprofile(user=user)
        user_profile.save()
post_save.connect(create_profile, sender=User)

class project(models.Model):
    filed_by = models.IntegerField(default=None,blank=False, null=True)

    boss_name = models.CharField(max_length=50,default=None,blank=False, null=True)
    boss_email=models.EmailField(default=None,blank=False, null=True)
    boss_mobile_number=models.CharField(max_length=10,default=None,blank=True, null=True)

    project_title = models.CharField(max_length=50,default=None,blank=False, null=True)
    project_description=models.TextField(default=None,blank=False, null=True)
    deadline=models.DateField(max_length=10,default=None,blank=False, null=True,help_text="Use %YYYY-%MM-%DD format.")
    resources=models.FileField(upload_to='files/',default=None,blank=False, null=True)

    employee_id = models.CharField(max_length=50,default=None,blank=False, null=True)
    employee_name = models.CharField(max_length=50,default=None,blank=False, null=True)

    file_submission=models.FileField(upload_to='files/',default=None,blank=False, null=True)
    Link_submission = models.URLField(max_length=50,default=None,blank=False, null=True)
    employee_mobile_number=models.CharField(max_length=10,default=None,blank=False, null=True)
