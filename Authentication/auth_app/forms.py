from django import forms
from django.contrib.auth.models import User
from auth_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio','profile_pic')

    # def __init__(self, *args, **kwargs):
    #     super(UserProfileInfoForm, self).__init__(*args, **kwargs)
    #     self.fields['profile_pic'].required = False
