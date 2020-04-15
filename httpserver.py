import argparse
import http.server
import socketserver
import urllib

global DATA


class RequestHandler(http.server.SimpleHTTPRequestHandler):

    def __pull_index_file(self):
        global DATA
        try:
            file_listener = urllib.URLopener()
            DATA = file_listener.retrieve("http://3.88.208.124/index.html", "test.html")
        except IOError:
            return None

    def do_GET(self):
        global DATA
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        if not DATA:
            self.__pull_index_file()
        self.wfile.write(bytes(DATA))


def main(port, origin):
    print("setting up server...")
    server_handler = http.server.SimpleHTTPRequestHandler
    http_serv = socketserver.TCPServer(("", port), server_handler)
    print("server set up. Checking for file...")
    print("Got file. Preparing to listen...")
    http_serv.serve_forever()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Take in a port and an origin, and spin up an HTTP server')
    parser.add_argument('-p', dest='port', type=str, help='The port on which to bind the HTTP server')
    parser.add_argument('-o', dest='origin', type=int, help='The origin where the CSN is')
    args = parser.parse_args()
    main(args.port, args.origin)

