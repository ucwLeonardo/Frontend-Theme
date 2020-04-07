# -*- coding: utf-8 -*-
from flask import Flask, Response, render_template, request

app = Flask(__name__, static_url_path='')


@app.route('/web')
def hello():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5353, threaded=True)
