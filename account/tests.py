from django.test import TestCase

# Create your tests here.


def test_login_page(client):
    resp = client.get('/account/login/')
    assert resp.status_code == 200


def test_register_page(client):
    resp = client.get('/account/register')
    assert resp.status_code == 200
