import io
import os
import socket
import struct

class Reader:

    def readByte(self,buffer):
        return int.from_bytes(buffer.read(1), 'big', signed=True)

    def readUnsignedByte(self,buffer):
        return int.from_bytes(buffer.read(1), 'big')

    def readUnsignedShort(self,buffer):
        return int.from_bytes(buffer.read(2), 'big')

    def readInt(self,buffer):
        return int.from_bytes(buffer.read(4), 'big', signed=True)

    def readDouble(self,buffer):        
        return struct.unpack('!d', buffer.read(8))[0]

    def readVarShort(self,buffer):
        ans = 0
        for i in range(0, 16, 7):
            b = self.readByte(buffer)
            ans += (b & 0b01111111) << i
            if not b & 0b10000000:
                return ans
        raise Exception("Too much data")

    def readVarInt(self,buffer):
        ans = 0
        for i in range(0, 32, 7):
            b = self.readUnsignedByte(buffer)
            ans += (b & 0b01111111) << i
            if not b & 0b10000000:
                return ans
        raise Exception("Too much data")

    def readVarUhInt(self,buffer):
        return self.readVarInt(buffer)