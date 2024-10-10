from fastapi.testclient import TestClient

from olympics import api


client = TestClient(api.app)


def test_countries():
    response = client.get('/countries/')
    assert response.status_code == 200
    assert len(response.json()) == 212

def test_athletes():
    response = client.get('/athletes/')
    assert response.status_code == 200
    assert len(response.json()) > 10000

def test_disciplines():
    response = client.get('/disciplines/')
    assert response.status_code == 200
    assert len(response.json()) == 45

def test_teams():
    response = client.get('/teams/')
    assert response.status_code == 200
    assert len(response.json()) > 1500

def test_events():
    response = client.get('/events/')
    assert response.status_code == 200
    assert len(response.json()) == 329

def test_medals():
    response = client.get('/medals/')
    assert response.status_code == 200
    assert len(response.json()) >= 1000

def test_discipline_athletes():
    response = client.get('/discipline-athletes/1')
    assert response.status_code == 200
    assert len(response.json()) >= 291

def test_top_countries():
    response = client.get('/top-countries/')
    assert response.status_code == 200
    assert len(response.json()) == 10

def test_collective_medals():
    response = client.get('/collective-medals/')
    assert response.status_code == 200
    assert len(response.json()) == 290

def test_individual_medals():
    response = client.get('/individual-medals/')
    assert response.status_code == 200
    assert len(response.json()) == 1

def test_top_individual():
    response = client.get('/top-individual/')
    assert response.status_code == 200
    assert len(response.json()) == 10