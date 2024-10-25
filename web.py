from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
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
"""
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