from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm

from .forms import PersonCreationForm, AirtimeForm
from .models import Permode, Datatype, Dataplan



        #   ....USER VALIDATION....

@unauthenticated_user
def registerPage(request):
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user= form.save()
			form.save()

			username = form.cleaned_data.get('username')


			messages.success(request, username + ' Account created Successfully...')
			return redirect ('login')

	context = {'form':form}
	return render(request, 'vtp/register.html', context)

# @unauthenticated_user
def loginPage(request):

	if request.method == 'POST': 
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('dashboard')
		
		else: messages.info(request, 'Username OR Password is incorect')


	context = {}
	return render(request, 'vtp/login.html', context)
    
def logoutUser(request):
	logout(request)
	return redirect('login')



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


def airtimeform(request):
    form = AirtimeForm()
    if request.method == 'POST':
        form = AirtimeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('airtime')
    return render(request, 'vtp/airtimeform.html', {'form': form})