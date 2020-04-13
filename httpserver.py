import argparse
import http.server
import socketserver


class HTTPServer:

    def __init__(self, port, origin):
        self.port = port
        self.origin = origin
        self.server_handler = http.server.SimpleHTTPRequestHandler

    def begin(self):
        print("setting up server...")
        http_serv = socketserver.TCPServer(("", self.port), self.server_handler)
        print("server set up. preparing to listen...")
        # TODO: Do we need to check if index exists, or can we assume it does
        # TODO: Do we assume that this server has the file, or should we go get it.
        http_serv.serve_forever()










if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Take in a port and an origin, and spin up an HTTP server')
    parser.add_argument('-p', dest='port', type=str, help='The port on which to bind the HTTP server')
    parser.add_argument('-o', dest='origin', type=int, help='The origin where the CSN is')
    args = parser.parse_args()
    server = HTTPServer(args.port, args.origin)

