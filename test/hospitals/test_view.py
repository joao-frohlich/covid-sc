import pytest
from django.urls import reverse
from .factories import HospitalFactory

pytestmark = pytest.mark.django_db

def test_hospital_detail_status_code(client):
    hospital = HospitalFactory()
    url = reverse('hospitals:detail', args=[hospital.id])
    response = client.get(url) 
    assert response.status_code == 200


def test_hospital_detail_templates(client, django_assert_num_queries):
    hospital = HospitalFactory()
    url = reverse('hospitals:detail', args=[hospital.id])
    with django_assert_num_queries(4):
        response = client.get(url)
    template_names = [template.name for template in response.templates]
    assert "hospital/show.html" in template_names
    assert "base.html" in template_names
    assert "Hospital of Konoha" in str(response.content)