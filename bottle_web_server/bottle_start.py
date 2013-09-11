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
    return headers + ''.join(request.body.readlines())


run(host='localhost', port=9191, reloader=True)

