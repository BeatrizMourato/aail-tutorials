from app import app

def test_ping():
    client = app.test_client()
    response = client.post(
        "/predict",
        json={"features": [5.1, 3.5, 1.4, 0.2]}
    )
    assert response.status_code == 200
    data = response.get_json()
    assert "prediction" in data

def test_predict_batch():
    client = app.test_client()
    response = client.post(
        "/predict-batch",
        json={"features": [
            [5.1, 3.5, 1.4, 0.2, 0.0, 1.0, 0.0, 0.0],
            [6.7, 3.0, 5.2, 2.3, 0.0, 0.0, 1.0, 0.0]
        ]}
    )
    assert response.status_code == 200
    data = response.get_json()
    assert "predictions" in data