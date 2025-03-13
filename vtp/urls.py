from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('dataform/', views.dataform, name='dataform'),
    path('<int:pk>/', views.person_update_view, name='person_change'),

    path('ajax/dataplan/', views.datatypes, name='dataplan'),
    path('ajax/load-datatypes/', views.datatypes, name='ajax_load_datatypes'), # AJAX
]