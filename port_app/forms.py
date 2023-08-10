from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre', max_length=100, widget=forms.TextInput(attrs={'class': 'form_input'}))
    email = forms.EmailField(label='Correo electrónico',widget=forms.TextInput(attrs={'class': 'form_input'}))
    message = forms.CharField(label='Mensaje', widget=forms.Textarea(attrs={'class': 'form_input'}))