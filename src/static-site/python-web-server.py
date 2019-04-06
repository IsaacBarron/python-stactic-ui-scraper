import http.server
import socketserver

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler


def run():
    print("Starting python web server".upper())
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port".upper(), PORT)
        httpd.serve_forever()


run()
