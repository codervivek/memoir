from django.shortcuts import render

# Create your views here.
from memoir.forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.db.models import Max
from django.views import generic
from django.contrib.auth.models import User
from memoir.forms import SignUpForm
from .models import Department,Professor,Category,CategoryList,Education,Work
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
from .crawling import get_cse_info

class ProfessorCreate(CreateView):
    model = Professor
    form_class=ProfessorForm
    def get_success_url(self):
        professor = self.object
        if professor.department.name == "CSE":
            person=get_cse_info(professor.mail,"uploads/photos/")
            if person:
                professor.photo="uploads/photos/"+professor.mail+".jpeg"
                professor.room_no=person["room"]
                professor.post=person["post"]
                professor.phone_office=person["phone"]
                professor.save()
                return reverse_lazy( 'professor-detail', kwargs={'pk': professor.id})
        return reverse_lazy( 'professor_update', kwargs={'pk': professor.id})

class ProfessorUpdate(UpdateView):
    model = Professor
    fields = ['user','department','photo','mail','mail_password','mail_server','post','room_no','phone_office','phone_home','qtr_no']

class ProfessorDelete(DeleteView):
    model = Professor

class EducationCreate(CreateView):
    model = Education
    fields = ['professor','degree','description']

class EducationUpdate(UpdateView):
    model = Education
    fields = ['degree','description']

class EducationDelete(DeleteView):
    model = Education
    def get_success_url(self):
        professor = self.object.professor
        return reverse_lazy( 'professor-detail', kwargs={'pk': professor.id})

class WorkCreate(CreateView):
    model = Work
    fields = ['professor','post','description']

class WorkUpdate(UpdateView):
    model = Work
    fields = ['post','description']

class WorkDelete(DeleteView):
    model = Work
    def get_success_url(self):
        professor = self.object.professor
        return reverse_lazy( 'professor-detail', kwargs={'pk': professor.id})

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
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

class SearchListView(generic.ListView):
    model = Professor

    def get_queryset(self):
        qs = Professor.objects.all()
        keywords = self.request.GET.get('q')
        if keywords:
            query = SearchQuery(keywords)
            vector = SearchVector('user__username', 'user__first_name', 'user__last_name')
            qs = qs.annotate(search=vector).filter(search=query)
            qs = qs.annotate(rank=SearchRank(vector, query)).order_by('-rank')

        return qs

def approve(request,pk,ck):
    x=CategoryList.objects.get(id=pk)
    x.approved=True
    print(x.data)
    x.save()
    return render(request, 'approve.html',{'x':ck})

def post_approve(request,pk):
    x=Professor.objects.get(id=pk)
    x.post=x.temp_post
    a=x.post
    x.temp_post=None
    x.save()
    return render(request, 'post_approve.html',{'x':pk,'a':a})

def post_delete(request,pk):
    x=Professor.objects.get(id=pk)
    x.temp_post=None
    x.save()
    return render(request, 'post_delete.html',{'x':pk})