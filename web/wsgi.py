#!/usr/bin/env python
def application(environ,start_response):
    start_response('200 OK',[('Content-Type','text/html')])
    return '<h1>Hello,Web!</h1>'
