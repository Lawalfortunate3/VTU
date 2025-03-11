from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import PersonCreationForm
from .models import Permode, Datatype

def dashboard(request):

	context = {}
	return render(request, 'vtp/dashboard.html', context)

def dataform(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dataform')
    return render(request, 'vtp/dataform.html', {'form': form})


def person_update_view(request, pk):
    permode = get_object_or_404(Permode, pk=pk)
    form = PersonCreationForm(instance=permode)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=permode)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'vtp/dataform.html', {'form': form})


# AJAX
def load_datatypes(request):
    network_id = request.GET.get('network_id')
    datatypes = Datatype.objects.filter(network_id=network_id).all()
    return render(request, 'vtp/datadd.html', {'datatypes': datatypes})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)

