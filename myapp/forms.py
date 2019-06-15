from django import forms

from .models import Notice
from django.contrib.auth import (
    authenticate,
    get_user_model

)

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter User id'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)
ROLE_CHOICES=[('student','Student'),('faculty','Faculty'),('other','Other...')]

class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Username'}))

    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter Email'}))

    password = forms.CharField(widget= forms.PasswordInput(attrs={'placeholder': 'Set Password'}))
    password2= forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}), label='Confirm Password')
    role = forms.CharField(label='Select your role?', widget=forms.Select(choices=ROLE_CHOICES))


    class Meta:
        model = User
        help_texts = {
            'username': None,
        }
        fields = [
            'username',
            'email',
            'password',
            'password2',
            'role'
        ]

    def clean(self, *args, **kwargs):

        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        role =  self.cleaned_data.get('role')
        if password != password2:
            raise forms.ValidationError(
                "Password do not match each other")
        if role!='faculty':
            raise forms.ValidationError(
                "Only Faculty can register")



            return super(UserRegisterForm, self).clean(*args, **kwargs)



class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = [
            'name' ,
            'message',
            'topic',


        ]

