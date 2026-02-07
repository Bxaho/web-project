from django import forms
from .models import Student


class studentForm(forms.ModelForm):

    class Meta:
        model=Student
        fields=['name','rollno','faculty','email','contact']
        # we exclude date of post and last updates because they are auto updated
