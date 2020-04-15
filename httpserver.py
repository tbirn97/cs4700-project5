import argparse
import http.server
import socketserver
import urllib
import socket

global DATA


class RequestHandler(http.server.SimpleHTTPRequestHandler):

    def __pull_index_file(self):
        global DATA
        try:
            print("trying to pull file")
            file_listener = urllib.URLopener()
            DATA = file_listener.retrieve("http://3.88.208.124/index.html", "test.html")
            print("file pulled")
        except IOError:
            return None

    def do_GET(self):
        global DATA
        print("do get")
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        if not DATA:
            self.__pull_index_file()
        print("Sending file")
        self.wfile.write(bytes(DATA))

def main(port, origin):
    print("Setting up server...")
    server_handler = http.server.SimpleHTTPRequestHandler
    local_ip = socket.gethostname()
    http_serv = socketserver.TCPServer((local_ip, port), server_handler)
    print(str(http_serv.server_address))
    print("Server set up.")
    print("Preparing to listen...")
    try:
        http_serv.serve_forever()
    except KeyboardInterrupt:
        pass
    http_serv.server_close()
    exit(0)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Take in a port and an origin, and spin up an HTTP server')
    parser.add_argument('-p', dest='port', type=int, help='The port on which to bind the HTTP server', required=True)
    parser.add_argument('-o', dest='origin', type=str, help='The origin where the CSN is', required=True)
    args = parser.parse_args()
    main(args.port, args.origin)

