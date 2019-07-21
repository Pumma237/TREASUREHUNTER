import io
import os
import socket
import struct

class Packet:

    def __init__(self):
        self.src_address = ""
        self.src_port = 0
        self.protocol = 0
        self.dst_address = ""
        self.dst_port = 0
        self.data = b''
        self.id = 0
        self.header = 0
        self.lenData = 0

    def __parse_ip_header(self, buffer):
        header = buffer.read(20)
        values = struct.unpack("!BBHHHBBH4s4s", header)
        ihl = values[0] & 0x0F
        self.src_address = socket.inet_ntoa(values[8])
        self.dst_address = socket.inet_ntoa(values[9])
        # Read the option bytes
        buffer.read((ihl * 4) - 20)
        self.protocol = values[6]

    def __parse_tcp_header(self, buffer):
        header = buffer.read(20)
        values = struct.unpack("!HHIIHHHH", header)
        self.src_port = values[0]
        self.dst_port = values[1]
        data_offset = values[4] >> 12
        # Read the option bytes
        buffer.read((data_offset * 4) - 20)

    def parse(self, buffer):
        self.__parse_ip_header(buffer)
        if self.protocol == 6:
            self.__parse_tcp_header(buffer)
            self.header = int.from_bytes(buffer.read(2),'big')
            self.lenData = int.from_bytes(buffer.read(self.header&3),'big')
            self.id=self.header>>2
        self.data = buffer.read()

    def __repr__(self):
        if self.protocol == 6:
            return "<TCP {0}>{1} {2}>".format(self.src_port, self.dst_port, self.id)
        return "<IP {0}>{1} {2}>".format(self.src_address, self.dst_address, self.id)

class Sniffer:

    def __init__(self, packet_filter=lambda: False):
        self.packet_filter = packet_filter
        # Due to windows limitation, we sniff from IP
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
        # We want the IP headers in the data received
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        # We want all the data related to our IP address
        host = socket.gethostbyname(socket.gethostname())
        self.sock.bind((host, 0))
        # In windows case, we have to confirm that we want to receive all.
        if os.name == "nt":
            self.sock.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    def __del__(self):
        # Deactivate the "receive all".
        if os.name == "nt":
            self.sock.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

    def recv(self):
        while True:
            buffer = io.BytesIO(self.sock.recv(2048))
            packet = Packet()
            packet.parse(buffer)
            if self.packet_filter(packet):
                return packet

def is_interesting(packet):
    if packet.protocol != 6:
        return False
    if packet.src_port != 5555 and packet.dst_port != 5555:
        return False
    if len(packet.data) == 0:
        return False
    return True

def main():
    sniffer = Sniffer(packet_filter=is_interesting)
    while True:
        packet = sniffer.recv()
        print(packet)

if __name__ == "__main__":
    main()