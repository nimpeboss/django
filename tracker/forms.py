from django import forms
from .models import Subject, StudySession

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name']

class StudySessionform(forms.ModelForm):
    class Meta:
        model = StudySession
        fields = ['subject', 'minutes', 'date']
