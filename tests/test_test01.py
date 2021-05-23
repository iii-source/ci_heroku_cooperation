import requests
import data


def test_1():
    a = 1
    b = 1
    assert a == b


def test_2():
    result = requests.get("http://127.0.0.1:5000/")
    print(result.text)
    assert result.text == "Hello World!"


def test_3():
    result = data.db_test03()
    for record in result['records']:
        assert record['test_id'] == 1



