from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Department(models.Model):

    name=models.CharField(max_length=150 ,help_text="Enter a new department")
    
    photo=models.FileField(upload_to='uploads/item/photos/', help_text="Upload a photo", null=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('department-detail', args=[str(self.id)])

class Professor(models.Model):

    user=models.OneToOneField(User,help_text="a",related_name="professor")

    department=models.ForeignKey(Department,help_text="Enter your department")

    mail=models.CharField(max_length=200, help_text="Enter email id to be searched")