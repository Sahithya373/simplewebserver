# EX01 Developing a Simple Webserver

## DATE: 01/10/2023

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
<LI> Walmart </LI>		
<LI> Apple </LI>
<LI> Cigna </LI>
<LI> Amazon.com, Inc </LI>
<LI> Vitol </LI>
</UL>
</body>
</html>
"""
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
```
## OUTPUT:
!![Alt text](<Screenshot (20).png>)

![Screenshot (19) - Copy](https://github.com/Sahithya373/simplewebserver/assets/147017926/0cb118b2-71e7-4c9f-888c-cf83fe4da79e)



## RESULT:
The program for implementing simple webserver is executed successfully.
