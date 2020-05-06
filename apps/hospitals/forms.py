from django import forms

from apps.hospitals.models import Patient


class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'birthday', 'airways', 'status', 'hospitalization_date', 'departure_date', 'cns', 'sisreg',
                  'departure_reason', ]
        widgets = {'airways': forms.RadioSelect(),
                   'status': forms.RadioSelect(),
                   'departure_reason': forms.RadioSelect(), }
