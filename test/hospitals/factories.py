import factory
from apps.hospitals.models import Hospital, City


class CityFactory(factory.DjangoModelFactory):
    class Meta:
        model = City


class HospitalFactory(factory.DjangoModelFactory):
    class Meta:
        model = Hospital

    city = factory.SubFactory(CityFactory)
    acronym = factory.Sequence(lambda n: f"Hospital #{n}")
    name = "Hospital of Konoha"
    phonenumber = "1231232323"
    email = "konoha@hospital"
