from .models import Professor, Category, CategoryList, Education, Work
from django import forms
from django.forms import ModelChoiceField

# class ProfessorRegisterForm(forms.ModelForm):
#     class Meta:
#         model=Professor


# class CategoryCreateForm(forms.ModelForm):
#     class Meta:
#         model=Category

# class FilterCategoryListForm(forms.Form):
#     category=forms.ModelChoiceField(queryset=Category.objects.all())
#     data=forms.CharField(max_length=10000, help_text="Enter information", widget=forms.Textarea)
#     def __init__(self, *args, **kwargs):
#         x=kwargs.pop('pk',None)
#         super(FilterCategoryListForm,self).__init__(*args,**kwargs)
#         professor=Professor.objects.get(id=x)
#         self.fields['category']=ModelChoiceField(queryset=professor.category_set.all())

class CategoryListForm(forms.Form):
    data=forms.CharField(max_length=10000, help_text="Enter information", widget=forms.Textarea)

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['user','department','mail','mail_password','mail_server','phone_home','qtr_no']
        widgets = {
            'mail_password': forms.PasswordInput()
        }