from django import forms
from HROCheckinApp.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ("first_name", "last_name", "password",)	# NOTE: the trailing comma is required