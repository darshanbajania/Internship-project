from django import forms
from django.contrib.auth.models import User
from .models import Book,Proposal,profile

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'pdf')

class ProposalForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['pdf']



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['image']