from flask import Flask # type: ignore
from flask import render_template # type: ignore

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template(
        'index.html'
    )

@app.route('/missing')
def missing():
    return render_template(
        'missing.html'
    )


@app.route('/worm')
def worm():
    return render_template(
        'worm.html'
    )


if __name__ == '__main__':
    app.run(debug=True)