from django.shortcuts import render, get_object_or_404
from .models import Versicles

# Create your views here.

def versicle_list(request):
    versicles = Versicles.objects.all()
    return render(request, 'versicles.html', {'versicles': versicles })

def versicle_teaching(request, pk):
    versicle = get_object_or_404(Versicles, pk=pk)
    return render(request, 'versicle_teaching.html', {'versicle': versicle})