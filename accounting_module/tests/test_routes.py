
"""
Unit tests for API routes.
"""

def test_get_accounts(client):
    response = client.get('/accounts')
    assert response.status_code == 200
