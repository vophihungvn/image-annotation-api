import pytest


def test_view(client):
    response = client.get('/api/v1/')
    assert response.status_code == 200
    assert b'success' in response.content
