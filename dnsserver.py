import argparse
import socket


class DNSServer:

    def __init__(self, name, port):
        self.name = name
        self.port = port

    def __given_name_get_host(self, name):
        return socket.gethostbyname(name)

    def __configure_socket(self):
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.bind((socket.gethostname(), self.port))
        return soc

    def listen(self):
        soc = self.__configure_socket()


def main(args):
    name = args.name
    port = args.port
    










if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Take in a name and a port, and spin up a DNS server bound')
    parser.add_argument('-n', dest='name', type=str, help='The CDN-specific name of the DNS server')
    parser.add_argument('-p', dest='port', type=int, help='The port on which to bind the DNS server')
    args = parser.parse_args()
    main(args)
