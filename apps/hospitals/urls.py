from django.urls import path

from . import views

urlpatterns = [
    path("", views.hospital_list, name ="hospital_list"),
    path("view/<int:pk>/", views.hospital_view, name ="hospital_view"),
    path("edit/<int:pk>/", views.hospital_update, name ="hospital_edit"),
]
