from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import ModelForm
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import CreateView, UpdateView

from apps.hospitals.forms import PatientForm
from apps.hospitals.models import Hospital, Patient, Report


def index(request):
    return render(request, "index.html", {})


class HospitalForm(ModelForm):
    class Meta:
        model = Hospital
        fields = ["name", "city", "phonenumber", "email"]


def hospital_list(request, template_name="hospitals/hospital_list.html"):
    hospital = Hospital.objects.all()

    data = {"object_list": hospital}
    return render(request, template_name, data)


def hospital_view(request, pk, template_name="hospitals/hospital_detail.html"):
    hospital = get_object_or_404(Hospital, pk=pk)

    report = Report.objects.filter(hospital=hospital).order_by("-report_date").first()

    data = {"object": hospital, "report": report}
    return render(request, template_name, data)


def hospital_update(request, pk, template_name="hospitals/hospital_form.html"):
    hospital = get_object_or_404(Hospital, pk=pk)

    form = HospitalForm(request.POST or None, instance=hospital)

    if form.is_valid():
        form.save()
        return redirect("hospitals:list")
    return render(request, template_name, {"form": form})


class PatientBaseView(LoginRequiredMixin):
    form_class = PatientForm
    template_name = 'hospitals/patient_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hospital'] = self.get_hospital()
        return context

    def get_hospital(self, pk='pk'):
        return Hospital.objects.get(pk=self.kwargs.get(pk))

    def get_success_url(self):
        return reverse('hospitals:detail', args=[self.get_hospital().pk, ])


class PatientCreateView(PatientBaseView, CreateView):
    def form_valid(self, form):
        patient = form.save(commit=False)
        patient.hospital = self.get_hospital()
        patient.save()

        messages.success(request=self.request, message="Paciente criado")
        return super(PatientCreateView, self).form_valid(form)


class PatientUpdateView(PatientBaseView, UpdateView):
    model = Patient

    def get_hospital(self, pk='hospital_pk'):
        return super().get_hospital(pk=pk)

    def form_valid(self, form):
        messages.success(request=self.request, message="Paciente atualizado")
        return super(PatientUpdateView, self).form_valid(form)
