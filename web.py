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