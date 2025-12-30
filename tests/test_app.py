"""Tests for the Flask application."""

import pytest
from app import app as flask_app

@pytest.fixture
def client():
    """Create and configure a new app instance for each test."""
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as testing_client:
        yield testing_client

def test_index(client):
    """Test the main endpoint."""
    response = client.get('/')
    assert response.status_code == 200
    expected_data = {
        "message": "Hello World!",
        "repository": "Hello-test-v1",
        "branch": "hello-v1"
    }
    assert response.json == expected_data

def test_health(client):
    """Test the health check endpoint."""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}
