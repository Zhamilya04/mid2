from django import forms
from .models import Course

class CourseRegistrationForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('name')

