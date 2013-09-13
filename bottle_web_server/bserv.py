__author__ = 'pacopablo'

from bottle import Bottle,route, run, template, request, post, get

app = Bottle()

@app.route('/')
def hello():
    return template('<b>Usage:<br><br> http://localhost:{{port}}/get <br> http://localhost:{{port}}/post</b>', port=8042)

@app.route('/post', method='POST')
def doPost():
    return do_response()


@app.route('/get', method='GET')
def doPost():
    return do_response()


def do_response():
    headers = ''
    body = ''
    for h in request.headers:
        headers += h + ": " + request.headers.get(h) + "\n"
    return headers + ''.join(request.body.readlines())
