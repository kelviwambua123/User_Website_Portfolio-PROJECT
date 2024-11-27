# portfolio/forms.py
from django import forms
from .models import Project, Tag

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'image', 'link', 'tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']