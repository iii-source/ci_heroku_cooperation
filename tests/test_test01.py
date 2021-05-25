import requests
import data


# 基本的な動作確認
def test_1():
    a = 1
    b = 1
    assert a == b


# APIの動作確認
def test_2():
    result = requests.get("http://127.0.0.1:5000/")
    print(result.text)
    assert result.text == "Hello"


# LocalDBの動作確認
def test_3():
    result = data.db_test()
    for record in result['records']:
        assert record['test_id'] == 1


# API経由でDBの動作確認
def test_4():
    result = requests.get("http://127.0.0.1:5000/db-test").json()
    for record in result['records']:
        assert record['test_id'] == 1



