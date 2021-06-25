from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import VenueForm


def inicio(request):
    return render(request,
     'inicio/inicio.html',
      {

      })

def entrevistador(request):
    return render(request,
     'inicio/entrevistador.html',
      {

      })
      
def add_venue(request):
  submitted = False
  if request.method == "POST":
    form = VenueForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('add_venue?submitted=True')
  else:
    form = VenueForm
    if 'submitted' in request.GET:
      submitted = True
			
  return render(request, 'inicio/add_venue.html', {
    'form': form, 'submitted':submitted
  })

def agenda(request):
    return render(request,
     'agenda/agenda.html',
      {

      })

def miUsuario(request):
    return render(request,
     'miUsuario/miUsuario.html',
      {

      })

def videollamada(request):
    return render(request,
     'videollamada/videollamada.html',
      {

      })