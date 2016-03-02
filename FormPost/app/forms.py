#*-* coding:utf-8 *-*

from django import forms

class FormContato(forms.Form):
    nome = forms.CharField()
    email = forms.EmailField()
    tell = forms.CharField(max_length=13)
    mess = forms.CharField(widget=forms.Textarea(),max_length=400)
