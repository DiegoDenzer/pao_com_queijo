from django.test import TestCase

# Create your tests here.


def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200


def test_login_page(client):
    resp = client.get('/auth/login/')
    assert resp.status_code == 200
