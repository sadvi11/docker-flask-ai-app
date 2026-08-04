import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))

import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home_endpoint(client):
    """Home endpoint returns service info."""
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['service'] == "AI Spam Classifier"


def test_health_endpoint(client):
    """Health check returns healthy status."""
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == "healthy"


def test_predict_spam(client):
    """A spammy message is classified as SPAM."""
    response = client.post('/predict', json={"text": "Win free money now click here"})
    assert response.status_code == 200
    data = response.get_json()
    assert data['prediction'] == "SPAM"
    assert 0 <= data['confidence'] <= 100


def test_predict_ham(client):
    """A normal message is classified as HAM."""
    response = client.post('/predict', json={"text": "Meeting at 3pm today confirmed"})
    assert response.status_code == 200
    data = response.get_json()
    assert data['prediction'] == "HAM"


def test_predict_missing_text(client):
    """Missing text field returns a 400 error."""
    response = client.post('/predict', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data
