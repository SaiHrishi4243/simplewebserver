# EX01 Developing a Simple Webserver
## Date: 25-10-2024
--
## AIM:
To develop a simple webserver to serve html pages and display the configuration details of laptop.

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
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
content = 
'''
<html>
    <body>
        My Laptop Configuration
        <table border="10" colspan="40" cellpadding="10">
            <tr>
                <th>System Configuration</th>
                <th>Description</th>
            </tr>
            <tr>
                <td>Processor</td>
                <td>13th Gen i5-1335U</td>
            </tr>
            <tr>
                <td>Primary Memory</td>
                <td>16 GB</td>
            </tr>
            <tr>
                <td>Secondary Memory</td>
                <td>300 GB</td>
            </tr>
            <tr>
                <td>Operation System</td>
                <td>Windows 11</td>
            </tr>
            <tr>
                <td>Graphics</td>
                <td>NVIDIA GeForce MX550</td>
            </tr>
        </table>
    </body>
</html>
'''
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request recieved")
        self.send_response(200)
        self.send_header('content-type','text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
"""

## OUTPUT:
![alt text](<Screenshot (4).png>)

![alt text](<Screenshot (5).png>)

## RESULT:
The program for implementing simple webserver is executed successfully.
