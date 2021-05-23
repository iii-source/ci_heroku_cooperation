from psycopg2.extras import DictCursor, psycopg2
import os

def test_1():
    a = 1
    b = 1
    assert a == b


def test_2():
    print(os.environ.get("DATABASE_URL"))
    connector = psycopg2.connect(os.environ.get("DATABASE_URL"))





