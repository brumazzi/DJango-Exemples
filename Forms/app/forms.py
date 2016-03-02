from django import forms

class FormPessoa(forms.Form):
    nome = forms.CharField(max_length=60)
    nasci = forms.DateTimeField(required=False)
    descri = forms.CharField(widget=forms.Textarea)
