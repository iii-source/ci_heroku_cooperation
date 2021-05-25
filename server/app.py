from flask import Flask
import os
import data


app = Flask(__name__)


# http://127.0.0.1:5000/
@app.route("/")
def hello():
    return "Hello"


@app.route('/db-test')
def db_test():
    result = data.db_test()
    return result


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
