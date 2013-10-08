from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Foo All The Things!'


if __name__ == '__main__':
    kwargs = {}
    kwargs.update({
        'host': '0.0.0.0',
        'port': 8080
    })
    app.run(**kwargs)
