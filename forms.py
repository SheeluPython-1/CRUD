from django import forms
from .models import Student
class AddStudentForm(forms.Form):
    name = forms.CharField()
    roll = forms.IntegerField()
    city = forms.CharField()
   