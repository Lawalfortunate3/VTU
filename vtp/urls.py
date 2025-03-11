from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('dataform/', views.dataform, name='dataform'),
    path('<int:pk>/', views.person_update_view, name='person_change'),


    path('ajax/load-datatypes/', views.load_datatypes, name='ajax_load_datatypes'), # AJAX
]