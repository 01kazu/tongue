from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from .models import Profile
from .models import Report
from django.forms import Textarea, TextInput


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input--style-3',
        'placeholder': 'username...'}))
    email = forms.EmailField(max_length=200, help_text='Required', widget=forms.TextInput(attrs={
        'class': 'input--style-3',
        'placeholder': 'e-mail..'}))
    
    # matric_number = forms.CharField(widget = forms.TextInput(attrs={
    #     'class': 'input--style-3',
    #     'placeholder': 'E.g BHU/16/04/05/9876'}))

    password1 = forms.CharField(widget = forms.PasswordInput(attrs={
        'class': 'input--style-3',
        'placeholder': 'password...',
    }))
    password2 = forms.CharField(widget = forms.PasswordInput(attrs={
        'class': 'input--style-3',
        'placeholder': 'confirm password...',
    }))
    # first_name = forms.CharField(max_length=50)
    # last_name = forms.CharField(max_length=50)

    # def clean(self):
    #     super(SignUpForm, self).clean()
    #     password1 = self.cleaned_data.get('password1')
    #     password2 = self.cleaned_data.get('password2')
    #     if password1 != password2:
    #         # self._errors['password1'] = self.error_class(["Passwords do not match!!!"])
    #     return self.cleaned_data

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    
class ReportForm(forms.ModelForm):
    # post = forms.CharField(widget= forms.Textarea(attrs={'placeholder': 'Post Something...'}))
    class Meta:
        model = Report
        fields = ('title','post', )
        widgets = {
            'title': TextInput(attrs = {'style': 'width: 50%; margin-bottom: 10px;', 'placeholder': "title..."}),
            'post' : Textarea(attrs= { 'rows': 10, 'class': "textarea", 'placeholder': "content...", 'style': 'width: 100%;'}),
        }

    
    # class ProfileForm(forms.ModelForm):
    #     matric_number = forms.CharField(widget = forms.TextInput(attrs={
    #     'class': 'input--style-3',
    #     'placeholder': 'E.g BHU/16/04/05/9876'}))

    #     class Meta:
    #         model = Profile
    #         fields = ("matric_number")

    
       



    