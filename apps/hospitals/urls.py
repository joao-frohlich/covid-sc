from django.urls import path

from . import views

urlpatterns = [
    path('', views.hospital_list, name='list'),
    path('<int:pk>/', views.hospital_view, name='detail'),
    path('<int:pk>/update/', views.hospital_update, name='update'),
    path('<int:pk>/patient/create/', views.PatientCreateView.as_view(), name='patient_create'),
    path('<int:hospital_pk>/patient/<int:pk>/update/', views.PatientUpdateView.as_view(), name='patient_update'),
]
