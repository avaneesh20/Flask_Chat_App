import requests


def test_api_post():
    payload = {'username': 'Avaneesh',
            'password': 'Test1'}
    resp = requests.post("http://127.0.0.1:5000/login", payload)
    assert (resp.status_code == 402), "Status code is not 402. Rather found : "\
        + str(resp.status_code)

    payload = {'username': 'Avaneesh1',
               'password': 'Test1'}
    resp = requests.post("http://127.0.0.1:5000/login", payload)
    assert (resp.status_code == 404), "Status code is not 403. Rather found : " \
                                      + str(resp.status_code)

    payload = {'username': 'Avaneesh',
               'password': 'Test'}
    resp = requests.post("http://127.0.0.1:5000/login", payload)
    assert (resp.status_code == 200), "Status code is not 200. Rather found : " \
                                      + str(resp.status_code)
