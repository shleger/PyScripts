__author__ = 'shleger'

from bottle import route, run, template, request, post, get


PORT = 9191


@route('/')
def index():
    return template('<b>Usage:<br><br> http://localhost:{{port}}/get <br> http://localhost:{{port}}/post</b>', port=PORT)


@post('/post') # or @route('/login', method='POST')
def doPost():
    return do_response()


@get('/get')
def doPost():
    return do_response()


def do_response():
    headers = ''
    body = ''
    for h in request.headers:
        headers += h + ":" + request.headers.get(h) + "\n"
    return headers + ''.join(request.body.readlines())


run(host='localhost', port=PORT, reloader=True)

