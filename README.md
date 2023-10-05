# EX01 Developing a Simple Webserver
## Date: 5/10/2023

## AIM:
To develop a simple webserver to serve html pages.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Serving the HTML pages.

### Step 5:
Testing the webserver.

## PROGRAM:
```
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
<title>My webserver</title>
</head>
<body>
<h1>Top 5 Revenue Generating Companies<h1>
<UL TYPE=“circle”>
<LI> Tata Consultancy Services Limited </LI>		
<LI> Tata MOtors </LI>
<LI> State Bank Of India </LI>
<LI> Amazon.com, Inc </LI>
<LI> Vitol </LI>
</UL>
</body>
</html>
```
class myhandler(BaseHTTPRequestHandler):
def do_GET(self):
print("request received")
self.send_response(200)
self.send_header('content-type', 'text/html; charset=utf-8')
self.end_headers()
self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()

## OUTPUT:
![5 COMPANIES](https://github.com/Sahithya373/simplewebserver/assets/147017926/d7315132-104b-41ca-9bf2-11d6e12c5fc5)

![SIMPLE SERVER OUTPUT](https://github.com/Sahithya373/simplewebserver/assets/147017926/5eac1821-018e-45d2-a66e-4653a9409137)

## RESULT:
The program for implementing simple webserver is executed successfully.
