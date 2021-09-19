from .models import Student,Scholarship
from django import forms
from django.contrib.auth.models import User



class StudentForm(forms.ModelForm):
    class Meta:

        model = Student

        fields = '__all__'
class ScholarshipForm(forms.ModelForm):
    class Meta:
        model=Scholarship
        fields='__all__'


