from flask.testing import FlaskClient

from loan import app
import pytest

# client -> act as a server to test the api endpoints
@pytest.fixture
def client():
    return app.test_client()

def test_home(client: FlaskClient):
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.data == b"<h1>Welcome to the Loan Application Service</h1>"

def test_predict(client):
    data = {
  "Gender": "Male",
  "Married": "No",
  "ApplicantIncome": 5000,
  "CreditHistory": 1,
  "LoanAmount": 1000
}

    resp = client.post("/predict", json=data)
    assert resp.status_code == 200
    assert resp.get_json() == {"Loan Status": "Loan Approved"}
