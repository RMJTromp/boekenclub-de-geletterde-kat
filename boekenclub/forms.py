from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm

from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio_text', 'city', 'date_of_birth']

        widgets = {
            'bio_text': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Tell us a bit about yourself...',
                'class': 'mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'
            }),
            'city': forms.TextInput(attrs={
                'placeholder': 'Your city',
                'class': 'mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'
            }),
            'date_of_birth': forms.DateInput(attrs={
                'type': 'date',
                'class': 'mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'
            }),
        }

        labels = {
            'bio_text': 'About Me',
            'date_of_birth': 'Birthday',
            'city': 'City / Town',
        }


class UserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Style the form fields
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'mt-1 block w-full px-3 py-2 bg-white border border-purple-200 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent transition duration-200'
            })

        # Custom labels
        self.fields['username'].label = 'Username'
        self.fields['email'].label = 'Email Address'
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Confirm Password'