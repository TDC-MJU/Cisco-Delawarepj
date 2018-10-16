#!/usr/bin/env python
import bottle as bt
from bottle import ServerAdapter
import cherrypy
import returnData

#This file should be located in /YourApp/py/
#Therefore, the file location should be /YourApp/py/runWebAppServer.py
#Do not forget to chmod 755 this file before running on your linux server

#'/' indicates http://IPhere
@bt.route('/', method = "GET")
def index():
    
    #index.html file should be in /YourApp/
    #Such that the function below points from the file location that webapp.py is in, to the directory above it
    
    f = open('../index.html')
    return f.read()

@bt.route('/css/<filename>', method = "GET")
def stylesheet(filename):
    #setting mime type to remove chrome error
    return bt.static_file(filename, root='../css/', mimetype='text/css')

@bt.route('/js/<filename>', method = "GET")
def jst(filename):
    f = open('../js/'+ filename )
    return f.read()

@bt.route('/py/<filename>', method = "GET")
def py(filename):
    return returnData.JSON()


@bt.route('/img/<filename>', method = "GET")
def jst(filename):
    f = open('../img/'+ filename )
    return f.read()

bt.debug(True)

class SSLCherryPyServer(ServerAdapter):
    def run(self, handler):
        from cherrypy import wsgiserver
        # from cherrypy.wsgiserver.ssl_pyopenssl import pyOpenSSLAdapter
        server = wsgiserver.CherryPyWSGIServer((self.host, self.port), handler)
        # server.ssl_adapter = pyOpenSSLAdapter('cacert.pem', 'privkey.pem')
        try:
            server.start()
        finally:
            server.stop()

#Set your host(Web Server IP) here, port 80 will only require you to type in the Web Server IP to access the web page

if __name__ == '__main__':
#Specify your server in host
#    bt.run(host='0.0.0.0', port=80, debug=True,server=SSLCherryPyServer)

#Running Locally
    bt.run(server=SSLCherryPyServer,port=5555, debug=True)