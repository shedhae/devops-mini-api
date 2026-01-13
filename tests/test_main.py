"""Tests for the DevOps Mini API."""
import sys
from pathlib import Path

# Add parent directory to path so we can import main
sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root_endpoint():
    """Test the root endpoint returns expected message."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "DevOps Mini API"}


def test_health_endpoint():
    """Test the health endpoint returns ok status."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_metrics_endpoint():
    """Test that Prometheus metrics endpoint is available."""
    response = client.get("/metrics")
    assert response.status_code == 200
    assert "python_info" in response.text
