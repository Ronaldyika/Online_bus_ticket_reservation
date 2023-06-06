from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"


class SignupForm(UserCreationForm):
    
    email = forms.EmailField(required=True)
    mobile_number = forms.CharField(required=True)
    city = forms.CharField(required=True)
    
    username = forms.CharField(help_text='', max_length=150)
    password1 = forms.CharField(help_text='', strip=False, widget=forms.PasswordInput)
    password2 = forms.CharField(help_text='', strip=False, widget=forms.PasswordInput)

    class Meta:
        model = AdminUser
        fields = ('username', 'email', 'mobile_number', 'city', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email address is already in use.')
        return email

class ChooseForm(forms.ModelForm):
    
    class Meta:
        model = Choose
        fields = '__all__'


class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomerRegistration
        fields = '__all__'
        
        def clean(self):
            clean_data = super(CustomerRegistrationForm, self).clean()
            current_destination = cleaned_data.get("current_destination")
            final_destination = cleaned_data.get("final_destination")
            
            if current_destination == final_destination:
                raise forms.ValidationError(
                    "Current destination and final destiantion must be different."
                    )
                
class SlideShowForm(forms.ModelForm):
    class Meta:
        model = SlideShow
        fields = '__all__'