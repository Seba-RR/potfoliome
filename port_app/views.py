
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.shortcuts import render
from portafolio.settings import EMAIL_HOST_USER
from .forms import ContactForm


def contact_view(request):
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            send_mail(
                f'Nuevo mensaje de contacto:',
                f'Nombre: {name}\nCorreo electrónico: {email}\nMensaje: {message}',
                'seba.ramirez.ramos@gmail.com',
                ['seba.ramirez.ramos@gmail.com',],  
                fail_silently=False,
            )
            request.session['email_sent'] = True
            return redirect('home', )
        else:
            request.session['email_sent'] = False
            print("Correo no enviando")
    return render(request, 'home.html', context)
