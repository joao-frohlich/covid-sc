from django.shortcuts import render
from django.views.generic.detail import DetailView
from apps.hospitals.models import Hospital, Report


def index(request):
    return render(request, 'index.html', {})


class HospitalDetailView(DetailView):
    model = Hospital
    template_name = 'hospital/show.html'

    def get_report(self):
        hospital = self.get_object()
        return Report.objects.filter(hospital=hospital).order_by('-report_date').first()
        

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['report'] = self.get_report()
        return context
