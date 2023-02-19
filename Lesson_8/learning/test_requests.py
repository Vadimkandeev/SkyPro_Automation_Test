import requests

def test_pass():
    resp = requests.get('https://dj-front.doct24.com/api/v1/reception_time/patient/get/58ce196f-3611-45ca-9ade-4d0dd3183c71')
    
    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "application/json; charset=utf-8"
    assert resp.text == ""

