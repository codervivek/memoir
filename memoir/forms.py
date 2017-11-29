from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, help_text='Enter your first name')
    last_name = forms.CharField(max_length=30,  help_text='Enter your last name')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', )
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        # for fieldname in ['username', 'password1', 'password2']:
        self.fields['password1'].help_text = 'Your password can\'t be too similar to your other personal information. Your password must contain at least 8 characters. Your password can\'t be a commonly used password. Your password can\'t be entirely numeric.'