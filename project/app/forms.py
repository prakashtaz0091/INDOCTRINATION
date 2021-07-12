from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Profile


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        





LEVEL_CHOICES =[
    ('teacher','teacher'),
    ('student','student'),      
]

DISABLED_CHOICES =[
    ('blind','Lost Vision'),
    ('deaf','Unable to Listen'),
    ('mute','Unable to Speak'),
]
class ProfileForm(forms.ModelForm):

    level = forms.ChoiceField(choices=LEVEL_CHOICES,widget=forms.RadioSelect)
    disabled = forms.ChoiceField(choices=DISABLED_CHOICES,widget=forms.RadioSelect,required=False)
    class Meta:
        model = Profile
        fields = ['name','address','phoneNo','dob','level','disabled']

        labels = {
            'name':'Full Name',
            'phoneNo':'Phone No',
            'dob': 'Date of Birth',
            'disabled':'If Disabled',
        }
