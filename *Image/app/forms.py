from django import forms

class ImageForm(forms.Form):
    name = forms.CharField(max_length=60,label="Nome da imagem")
    file = forms.ImageField()

    def __str__(self):
        return self.as_table()
