from Reader import Reader
import io
import os
import socket
import struct
import pdb;pause=pdb.set_trace
import math
class TreasureHuntDigRequestAnswerMessage:

    def __init__(self):
        self.questype=0
        self.result= None
        self.data = b''
    def deserialize(self,buffer):

        reader=Reader()
        print("84 is here")
        self.questype = reader.readByte(buffer)
        print("questype = {0}".format(self.questype))

        self.result = reader.readByte(buffer)
        print("result = {0}".format(self.result))
    def __repr__(self):
        print("questype = {0}/result = {1}".format(self.questype,self.result))