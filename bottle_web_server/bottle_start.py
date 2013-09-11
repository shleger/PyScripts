__author__ = 'shleger'

from bottle import route, run, template, request, post


@route('/hello/<name>')
def index(name='World'):
    print " dd: "

    return template('<b>Hello {{name}}</b>!', name=name)


@post('/post') # or @route('/login', method='POST')
def do_login():

    headers = ''
    body = ''
    for h in request.headers:
        headers += h + ":" + request.headers.get(h) + "\n"
    for b in request.body :
        body += b

    # headers = request.headers
    # body = request.body.readlines()

    return headers + body


run(host='localhost', port=8080)

