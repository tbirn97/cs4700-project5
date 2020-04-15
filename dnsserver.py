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

    def make_query_section(self, queries):
        return self.name + b'\x00\x01' + b'\x00\x01'

    def make_answer_section(self, queries):
        compression = b'\xc0\x0c'
        ttl = (400).to_bytes(4, byteorder='big')

        ipaddr = b'\xff\xff\xff\xff'
        return compression + b'\x00\x01' + b'\x00\x01' + ttl + b'\x00\x04' + ipaddr


    def __make_response(self, data):
        #transaction id
        tid = data[0:2]
        #flags header
        flags = flags_build(data[2:4])
    
        #question count
        qdcount = b'\x00\x01'

        #setup for answer count value
        queries = data[12:] #strip the dns header
        
        #answer count of one because there is only one ip
        ancount = b'\x00\x01'
    
        #nameserver count
        nscount = b'\x00\x00'

        #additional count
        addcount = b'\x00\x00'

        #dns header
        hdr = tid + flags + qdcount + ancount + nscount + addcount

        print("header: ", hdr)

        #query section
        q_sec = self.make_query_section(queries)

        print("query section: ", q_sec)

        #make answer section
        a_sec = self.make_answer_section(queries)

        return hdr + q_sec + a_sec

  

    def listen(self):
        soc = self.__configure_socket()
        while True:
            data, addr = sock.recvfrom(512)
            #TODOneeds to respond to dns queries using the response maker here           


def main(args):
    name = args.name
    port = args.port
    dns = DNSServer(name, port)
    #dns.listen 










if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Take in a name and a port, and spin up a DNS server bound')
    parser.add_argument('-n', dest='name', type=str, help='The CDN-specific name of the DNS server')
    parser.add_argument('-p', dest='port', type=int, help='The port on which to bind the DNS server')
    args = parser.parse_args()
    main(args)
