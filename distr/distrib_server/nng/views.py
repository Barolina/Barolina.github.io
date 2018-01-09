from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from nng.models import NNGModel


def _index(request):
    return HttpResponse('est')

class index(ListView):
    queryset = NNGModel.objects.all()
    template_name = 'index.html'
    context_object_name = 'obj'