from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http.response import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.contrib import messages

from forms import *
from models import Denuncia


def home(request):
    return render_to_response('home.html', {}, 
        context_instance=RequestContext(request))

def legislacion(request):
    return render_to_response('legislacion.html', {}, 
        context_instance=RequestContext(request))

def quienes_somos(request):
    return render_to_response('quienes_somos.html', {}, 
        context_instance=RequestContext(request))

def como_funciona(request):
    return render_to_response('como_funciona.html', {}, 
        context_instance=RequestContext(request))

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Mensaje enviado')
            nombre = form.cleaned_data["Nombre"]
            email = form.cleaned_data["Email"]
            asunto = form.cleaned_data["Asunto"]
            comentario = form.cleaned_data["Comentario"]
            comentario = "De: "+email+"\n"+ \
                            "Asunto: "+asunto+"\n"+ \
                            "Mensaje: "+comentario

            send_mail(asunto, comentario, email, 
                ['carry@mailinator.com'], fail_silently=False)
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.warning(request, 'Por favor complete los campos.')
    else:
        messages.info(request, 'Complete los campos.')
        form = ContactoForm()
    data = {'form' : form}
    return render_to_response('contacto.html', data, 
        context_instance=RequestContext(request))

def denunciar(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = DenunciaForm(request.POST, request.FILES) 
        imagen = None
        if form.is_valid():
            messages.success(request, 'Denuncia enviada')
            nombre = form.cleaned_data["Nombre"]
            apellido = form.cleaned_data["Apellido"]
            dni = form.cleaned_data["DNI"]
            telefono = form.cleaned_data["Telefono"]
            email = form.cleaned_data["Email"]
            denunciado = form.cleaned_data["Denunciado"]
            rubro = form.cleaned_data["Rubro"]
            direccion = form.cleaned_data["Direccion"]
            provincia = form.cleaned_data["Provincia"]
            ciudad = form.cleaned_data["Ciudad"]
            descripcion = form.cleaned_data["Descripcion"]
            try:
                # TODO Arreglar este parche feo
                imagen = request.FILES['Imagen']
            except Exception:
                pass
            denuncia = Denuncia(nombre = nombre, 
                                apellido = apellido,
                                dni = dni,
                                telefono = telefono,
                                email = email,
                                denunciado = denunciado,
                                rubro = rubro,
                                direccion = descripcion,
                                provincia = provincia,
                                ciudad = ciudad,
                                descripcion = descripcion,
                                imagen = imagen)
            denuncia.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.warning(request, 'Por favor complete los campos.')
    else:
        messages.info(request, 'Complete el formulario.')
        form = DenunciaForm()
    data = {
        'form': form,
    }   
    return render_to_response('denunciar.html', data, 
        context_instance=RequestContext(request))

def enviar_denuncia(request):
    return render_to_response('enviar_denuncia.html', {}, 
        context_instance=RequestContext(request))

