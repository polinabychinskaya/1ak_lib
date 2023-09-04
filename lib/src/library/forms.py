from django import forms
from django.contrib.auth.models import User
from . import models

class IssueBookForm(forms.Form):
    isbn2 = forms.ModelChoiceField(
        queryset=models.Book.objects.all(), 
        empty_label="Название (ISBN)", 
        to_field_name="isbn", 
        label="Информация о книге")
    name2 = forms.ModelChoiceField(
        queryset=models.Reader.objects.all(), 
        empty_label="Полное имя", 
        to_field_name="user", 
        label="Информация о читателе")
    
   
