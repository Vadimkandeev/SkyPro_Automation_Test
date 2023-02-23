import requests

base_url = "https://x-clients-be.onrender.com"



def test_simple_req():
    resp = requests.get(base_url + '/company')
    response_body = resp.json()
    first_company = response_body[0]
    assert first_company["name"] == "Барбершоп 'ЦирюльникЪ'"
    assert resp.status_code == 200   
    assert resp.headers["Content-Type"] == "application/json; charset=utf-8"




def test_auth():
    creds = {
        'username': 'bloom',
        'password': 'fire-fairy'
    }
    resp = requests.post(base_url + '/auth/login', json=creds)
    token = resp.json()["userToken"]
    assert resp.status_code == 201
    
    #response_body = resp.json()


def test_create_company():
    creds = {
        'username': 'bloom',
        'password': 'fire-fairy'
    }
    company = {
        'name': 'Python',
        'description': 'Classess_Python'
    }
     # authorization
    resp = requests.post(base_url + '/auth/login', json=creds)
    token = resp.json()["userToken"]

    # creation
    my_headers = {}
    my_headers["x-client-token"] = token
    resp = requests.post(base_url + '/company', json=company, headers=my_headers)
    assert resp.status_code == 201


 

   
    