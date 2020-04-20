import argparse
import socket


class DNSServer:

    def __init__(self, name, port):
        self.name = name
        self.port = port

    def local_name_resolution(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(('10.255.255.255', 1))
            localip = s.getsockname()[0]
        except:
            localip = '127.0.0.1'
        finally:
            s.close()
        return localip


    def __configure_socket(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #localip = self.local_name_resolution()
        localip = '127.0.0.1'
        self.sock.bind((localip, self.port))
        #print(self.sock)

    def make_flags(self, data):
        qr = '1'
        #print(data)
        opcode = ''.join([str(ord(data[0:1])&(1<<b)) for b in range(1,5)])
        aa = '1'
        tc = '0'
        rd = '0'
        ra = '0'
        z = '000'
        rcode = '0000'
        flags = int(''.join([qr, opcode, aa, tc, rd, ra, z, rcode]), 2)
        return flags.to_bytes(2, byteorder='big')

    def make_query_section(self, queries):
        return self.get_name() + b'\x00\x01' + b'\x00\x01'

    def get_name(self):
        seg_len = 0
        bytes_name = b''
        name = self.name
        for character in name:
            if character == '.':
                bytes_name = bytes_name + seg_len.to_bytes(1, 'big') + bytes(name[:seg_len], 'utf-8')
                #print("length: ", str(seg_len), "\nbytes: ", str(bytes_name))
                name = name[seg_len+1:]
                seg_len = 0
            else:
                seg_len += 1
        bytes_name = bytes_name + seg_len.to_bytes(1, 'big') + bytes(name, 'utf-8') + b'\x00'
        #print("length: ", str(seg_len), "\n bytes: ", str(bytes_name))
        return bytes_name
    def make_answer_section(self, queries):
        compression = b'\xc0\x0c'
        ttl = (400).to_bytes(4, byteorder='big')
        ipaddr = self.local_name_resolution()
        ipaddr = socket.inet_aton(ipaddr)
        #ipaddr = b'\xff\xff\xff\xff'
        answer = compression + b'\x00\x01' + b'\x00\x01' + ttl + b'\x00\x04' + ipaddr
        #print("answer: ", str(answer))
        return answer


    def __make_response(self, data):
        #transaction id
        tid = data[0:2]
        #flags header
        #print("transaction id: ", str(tid))

        flags = self.make_flags(data[2:4])
        #print("flags: ", str(flags))

    
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

        #print("header: ", hdr)

        #query section
        q_sec = self.make_query_section(queries)

        #print("query section: ", q_sec)

        #make answer section
        a_sec = self.make_answer_section(queries)

        response = hdr + q_sec + a_sec
        return response

  

    def listen(self):
        self.__configure_socket()
        #print(self.sock)
        while True:
            data, addr = self.sock.recvfrom(512)
            #print(data)
            if not data: break
            response = self.__make_response(data)
            #print(response)
            #print(addr)
            self.sock.sendto(response, addr)
    def close(self):
        self.sock.close()


def main(args):
    name = args.name
    port = args.port
    dns = DNSServer(name, port)
    dns.listen()
    try:
        dns.listen()
    except KeyboardInterrupt:
        pass
    dns.close()
    exit(0)










if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Take in a name and a port, and spin up a DNS server bound')
    parser.add_argument('-n', dest='name', type=str, help='The CDN-specific name of the DNS server')
    parser.add_argument('-p', dest='port', type=int, help='The port on which to bind the DNS server')
    args = parser.parse_args()
    main(args)
