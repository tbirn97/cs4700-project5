import argparse
import http.server
import socketserver
import urllib.request
import socket


class RequestHandler(http.server.SimpleHTTPRequestHandler):


    def get_file_bytes(self):
        try:
            f = open("index.html", "r")
            data = f.read()
            return bytes(data)
        except IOError:
            print("fetching file")
            data = self.pull_index_file()
            f = open("index.html", "w+")
            f.write(str(data))
            data = f.read()
            return bytes(data)
        finally:
            f.close()
            
            
    def pull_index_file(self):
        try:
            print("trying to pull file")
            if is_cache:
            response = urllib.request.urlopen("http://3.88.208.124/index.html")
            return response.read()
        except IOError:
            return None

    def do_GET(self):
        print("do get")
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        data = self.get_file_bytes()
        print("Sending file...")
        self.wfile.write(data)
    


def main(port, origin):
    print("Setting up server...")
    server_handler = RequestHandler
    local_ip = socket.gethostname()
    http_serv = socketserver.TCPServer((local_ip, port), server_handler)
    print("Server set up. Preparing to listen...")
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

