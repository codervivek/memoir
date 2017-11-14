from django.shortcuts import render

# Create your views here.
from memoir.forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.db.models import Max
from django.views import generic
from django.contrib.auth.models import User
from memoir.forms import SignUpForm
from .models import Department,Professor,Category,CategoryList
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('professor_create')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def home(request):
    department=Department.objects.all()
    return render(request,'index.html', {'department_list':department})

class ProfessorDetailView(generic.DetailView):
    model=Professor

class DepartmentListView(generic.ListView):
    model=Department

class DepartmentDetailView(generic.DetailView):
    model=Department

class CategoryDetailView(generic.DetailView):
    model=Category


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ProfessorForm

class ProfessorCreate(CreateView):
    model = Professor
    form_class=ProfessorForm

class ProfessorUpdate(UpdateView):
    model = Professor
    fields = ['user','department','photo','mail','mail_password','post','room_no','phone_office','phone_home','qtr_no']

class ProfessorDelete(DeleteView):
    model = Professor

class CategoryCreate(CreateView):
    model = Category
    fields = ['professor','name','search_text','to_crawl']

class CategoryUpdate(UpdateView):
    model = Category
    fields = ['search_text','to_crawl']

class CategoryDelete(DeleteView):
    model = Category
    def get_success_url(self):
        professor = self.object.professor
        return reverse_lazy( 'professor-detail', kwargs={'pk': professor.id})

# class CategoryListCreate(CreateView):
#     model = CategoryList
#     fields = ['category','data']

class CategoryListUpdate(UpdateView):
    model = CategoryList
    fields = ['data']

class CategoryListDelete(DeleteView):
    model = CategoryList
    def get_success_url(self):
        category = self.object.category
        return reverse_lazy( 'category-detail', kwargs={'pk': category.id})

from .forms import CategoryListForm
from django.shortcuts import redirect


def categorylist_create(request,pk):
    if request.method=='POST':
        form=CategoryListForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data['data']
            cat=Category.objects.get(id=pk)
            new_cat_list=CategoryList.objects.create(category=cat,data=data)
            new_cat_list.save()
            return redirect('category-detail',pk=pk)
        else:
            form=CategoryListForm()
    else:
        form=CategoryListForm()
    return render(request,'profiles/categorylist_form.html',context={'form':form})

