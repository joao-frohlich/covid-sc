from django.forms import ModelForm
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView

from apps.hospitals.models import Hospital, Occupation, Report


def index(request):
    return render(request, "index.html", {})

class HospitalForm(ModelForm):
    class Meta:
        model = Hospital
        fields = ["name"]


def hospital_list(request, template_name="hospitals/hospital_list.html"):
    hospital = Hospital.objects.all()
    data = {"object_list": hospital}

    return render(request, template_name, data)


def hospital_view(request, pk, template_name="hospitals/hospital_detail.html"):
    hospital = get_object_or_404(Hospital, pk=pk)
    report = Report.objects.filter(hospital=hospital).order_by("-report_date").first()
    data = {"object":hospital, "report":report}

    return render(request, template_name, data)


def hospital_update(request, pk, template_name="hospitals/hospital_form.html"):
    hospital = get_object_or_404(Hospital, pk=pk)
    form = HospitalForm(request.POST or None, instance=hospital)
    if form.is_valid():
        form.save()
        return redirect("hospital_list")

    return render(request, template_name, {"form":form})
