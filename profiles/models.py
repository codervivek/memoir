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

    user=models.OneToOneField(User,help_text="a",related_name='professor')

    department=models.ForeignKey(Department,help_text="Enter your department")

    photo=models.ImageField(upload_to="uploads/photos/", help_text="Upload your profile picture", default="default_pic.png", blank=True, null=True)

    mail=models.CharField(max_length=200, help_text="@iitg.ernet.in", blank=True, null=True)

    mail_password=models.CharField(max_length=200,help_text="Enter your password", blank=True, null=True)

    SERVERS = (
        ('0', 'Teesta'),
        ('1', 'Naambor'),
        ('2', 'Disang'),
        ('3', 'Tamdil'),
        ('4', 'Dikrong')
    )

    mail_server=models.CharField(max_length=2, choices=SERVERS,blank=True, null=True, default='4', help_text="Select your webmail server")

    post=models.CharField(max_length=200, help_text="Enter your post", blank=True, null=True)

    room_no=models.CharField(max_length=200, help_text="Enter your room no.", blank=True, null=True)

    phone_office=models.CharField(max_length=200, help_text="Enter your office phone no.", blank=True, null=True)

    phone_home=models.CharField(max_length=200, help_text="Enter your home phone no.", blank=True, null=True)

    qtr_no=models.CharField(max_length=200, help_text="Enter your qtr no.", blank=True, null=True)

    search_start=models.IntegerField(default=0)

    temp_post=models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def crawl_prof(self):
        z=crawl_print(self.mail,self.mail_password,
        "promoted",int(self.mail_server),re.compile('\"(.*?)\"'),self.search_start)
        x=Professor.objects.get(id=self.id)
        x.search_start=z['end']
        x.save()
        if z["messages"]:
            for y in z['messages']:
                w=Professor.objects.get(id=self.id)
                w.temp_post=y
                w.save()
        return ""

    def get_absolute_url(self):
        return reverse('professor-detail', args=[str(self.id)])

from .crawling import crawl_print
import re

class Category(models.Model):

    professor=models.ForeignKey(Professor,help_text="a",on_delete=models.CASCADE)

    name=models.CharField(max_length=100,help_text="Enter category")

    search_text=models.CharField(max_length=1000,help_text="Search keyword for crawling mail", blank=True, null=True)

    to_crawl=models.BooleanField(default=False, help_text="Enable/Disable webmail crawling for this category")

    search_start=models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def crawl_category(self):
        z=crawl_print(self.professor.mail,self.professor.mail_password,
        self.search_text,int(self.professor.mail_server),re.compile('\"(.*?)\"'),self.search_start)
        x=Category.objects.get(id=self.id)
        x.search_start=z['end']
        x.save()
        for y in z['messages']:
            w=CategoryList.objects.create(category=self,data=y,approved=False)
            w.save()
        return ""

    def get_absolute_url(self):
        return reverse('category-detail', args=[str(self.id)])

class CategoryList(models.Model):

    category=models.ForeignKey(Category,help_text="Enter category data",on_delete=models.CASCADE)

    data=models.TextField(max_length=10000, help_text="Enter data")

    approved=models.BooleanField(default=True)

    def __str__(self):
        return self.data[:20]

    def get_absolute_url(self):
        return reverse('category-detail', args=[str(self.category.id)])

class Education(models.Model):

    degree=models.CharField(max_length=200, help_text="Enter your degree", blank=True, null=True)

    professor=models.ForeignKey(Professor, help_text="b")

    description=models.CharField(max_length=200, help_text="Enter degree description", blank=True, null=True)

    def __str__(self):
        return self.degree

    def get_absolute_url(self):
        return reverse('professor-detail', args=[str(self.professor.id)])

class Work(models.Model):

    post=models.CharField(max_length=200, help_text="Enter your Post", blank=True, null=True)

    professor=models.ForeignKey(Professor, help_text="b")

    description=models.CharField(max_length=200, help_text="Enter Post description", blank=True, null=True)

    def __str__(self):
        return self.post

    def get_absolute_url(self):
        return reverse('professor-detail', args=[str(self.professor.id)])