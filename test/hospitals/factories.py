import factory
from apps.hospitals.models import Hospital


class HospitalFactory(factory.DjangoModelFactory):
    class Meta:
        model = Hospital
    
    acronym = factory.Sequence(lambda n: f"Hospital #{n}")
    name = "Hospital of Konoha"
    city = "Konoha"
    phonenumber = "1231232323"
    email = "konoha@hospital"