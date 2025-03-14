from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import PersonCreationForm, AirtimeForm
from .models import Permode, Datatype, Dataplan

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
def datatypes(request):
    network_id = request.GET.get('network_id')
    datatypes = Datatype.objects.filter(network_id=network_id).all()
    print(list(datatypes.values('id', 'name')))
    # return render(request, 'vtp/datadd.html', {'datatypes': datatypes})
    return JsonResponse(list(datatypes.values('id', 'name')), safe=False)

def dataplan(request):
    datatype_id = request.GET.get('datatype_id')
    dataplan = Dataplan.objects.filter(datatype_id=datatype_id).all()
    print(list(dataplan.values('id', 'name')))
    # return render(request, 'vtp/datadd.html', {'datatypes': datatypes})
    return JsonResponse(list(dataplan.values('id', 'name')), safe=False)






        # ....AIRTIME VIEW....


def airtime(request):
    form = AirtimeForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('airtime')
    return render(request, 'vtp/airtime.html', {'form': form})