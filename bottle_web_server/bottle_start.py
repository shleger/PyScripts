__author__ = 'shleger'

from bottle import route, run, template, request, post, get, static_file, response, HTTPResponse
import time


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



@post('/fns36-reg/create-signed')
def doCreateSigned():
    response.status = 201

    #response = HTTPResponse(status=201, body='<html/>')
    response.set_header('X-AspNetMvc-Version', '3.0')
    #response.set_header('Server', 'nginx')
    response.set_header('X-AspNet-Version', '4.0.30319')
    response.set_header('X-Powered-By', 'ASP.NET')
    response.set_header('Location', '/fns36-reg/A7585B5F28625D47A71535C6EA59E2F1')
    response.set_header('Cache-Control', 'private')
    response.set_header('Connection', 'keep-alive')
    response.set_header('Link', '<http://localhost/fns36-reg/A7585B5F28625D47A71535C6EA59E2F1/regcard>;rel=fns36-reg-regcard, <http://localhost/fns36-reg/A7585B5F28625D47A71535C6EA59E2F1/status>;rel=fns36-reg-status')
    response.set_header('Content-Length', '0')

    #	hdr = {'Location': 'http://localhost/fns36-reg/A7585B5F28625D47A71535C6EA59E2F1'}
    #    return HTTPResponse(status=201, body='', headers=hdr)

    return response

# return response

@route('/fns36-reg/inspection-certs')
def downloadCerts():
    return static_file('certs.zip', root='D:/workspace_py/handleProcess/bottle_web_server', download='certs.zip')

def do_response():
    headers = ''
    body = ''
    for h in request.headers:
        headers += h + ":" + request.headers.get(h) + "\n"
    return headers + ''.join(request.body.readlines())


run(host='0.0.0.0', port=PORT, reloader=True, debug=True, server='paste')

