from psycopg2.extras import DictCursor, psycopg2
import os


# DBセッション開始
def get_connection():
    dsn = os.environ.get('DATABASE_URL')
    return psycopg2.connect(dsn)


# DB接続 + クエリ返却テスト
def db_test():
    with get_connection() as conn:
        with conn.cursor(cursor_factory=DictCursor) as cur:
            cur.execute('SELECT * FROM test_table where test_id = 1')
            result = cur.fetchall()

            result_list = []
            result_dict = {}
            for row in result:
                # DictRowをdict変換
                result_list.append(dict(row))
            result_dict['records'] = result_list

            return result_dict
