#!/usr/bin/env python
from wsgiref.simple_server import make_server
from wsgiapp import application 
httpd = make_server('',8000,application)
print httpd
print "Serving on Port 8000..."
httpd.serve_forever()
