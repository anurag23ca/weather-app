from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_weather_records_no_filter():
    '''
    Test weather record endpoint
    '''
    response = client.get("/api/weather/")
    assert response.status_code == 200
    assert len(response.json()) == 10


def test_read_weather_records_filter_by_date():
    '''
    Test that only objects with date '19850101' are returned
    '''
    response = client.get("/api/weather/?date=19850101")
    assert response.status_code == 200
    assert response.json()[0]["date"] == 19850101


def test_read_weather_records_filter_by_station_id():
    '''
    Test that only objects with station_id 'USC00110072' are returned
    '''
    response = client.get("/api/weather/?station_id=USC00110072")
    assert response.status_code == 200
    assert all(data["station_id"] == "USC00110072" for data in response.json())


def test_read_weather_stats_no_filter():
    '''
    Test weather stats endpoint
    '''
    response = client.get("/api/weather/stats")
    assert response.status_code == 200
    assert len(response.json()) == 10


def test_read_weather_stats_filter_by_year():
    '''
    Test that only objects with year '1985' are returned
    '''
    response = client.get("/api/weather/stats?year=1985")
    assert response.status_code == 200
    assert all(data["date"].startswith("1985") for data in response.json())


def test_read_weather_stats_filter_by_station_id():
    '''
    Test that only objects with station_id 'USC00110072' are returned
    '''
    response = client.get("/api/weather/stats?station_id=USC00110072")
    assert response.status_code == 200
    assert response.json()[0]["station_id"] == "USC00110072"
