from flask import Flask
app = Flask('foo')


@app.route('/')
def hello_world():
    return 'Foo All The Things!'


if __name__ == '__main__':
    app.config.from_object('foo.config')  # Default

    kwargs = {}
    kwargs.update({
        'host': '0.0.0.0',
        'port': 8080
    })

    app.run(**kwargs)
