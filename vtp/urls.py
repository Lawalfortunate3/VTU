from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	#Leave as empty string for base url
    path('', views.dashboard, name="dashboard"),
    # path('person_create_view/', views.person_create_view, name="person_create_view"),

    path('dataCreate/', views.dataCreate, name='dataCreate'),
    path('<int:pk>/', views.dataUpdate, name='dataUpdate'),


    path('ajax/load_datatype/', views.load_datatype, name='ajax_load_datatype'), # AJAX
]