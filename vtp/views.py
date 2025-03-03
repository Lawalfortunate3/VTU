from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import * 
from .forms import DataForm
from .models import Network, DataType

# Create your views here.   


def dashboard(request):

	context = {}
	return render(request, 'vtp/dashboard.html', context)

def dataCreate(request):
    form = DataForm() 
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dataCreate')
    return render(request, 'vtp/dataCreate.html', {'form': form})


def dataUpdate(request, pk):
    dataRequest = get_object_or_404(ReqData, pk=pk)
    form = DataForm (instance=dataRequest)
    if request.method == 'POST':
        form = DataForm (request.POST, instance=dataRequest)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'persons/home.html', {'form': form})

  
# AJAX
def load_datatype(request):  
    network_id = request.GET.get('network_id')
    datatypes = DataType.objects.filter(network_id=network_id)
    # return render(request, 'vtu/city_dropdown_list_options.html', {'cities': cities})
    print(list(datatypes.values('id', 'name')))
    return JsonResponse(list(datatypes.values('id', 'name')), safe=False)

  