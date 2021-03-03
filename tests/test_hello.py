import requests


def test1():
    get_url_info = requests.get('http://127.0.0.1:5000/')
    print(get_url_info)
    assert get_url_info.status_code == 200


