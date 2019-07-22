from Reader import Reader
import io
import os
import socket
import struct
import pdb;pause=pdb.set_trace
import math
class TreasureHuntMessage:

    def __init__(self):
        self.questype=0
        self.mapid= None
        self.knownStepsListLen=None
        self.liste1 =[]
        self.totalStepCount=None
        self.checkPointCurrent=0
        self.checkPointTotal=0
        self.availableRetryCount=None
        self.flagsLen=None
        self.liste2 =[]
        self.liste3 =[]
        self.liste = []
        self.data = b''
    def deserialize(self,buffer):

        reader=Reader()

        self.questype = reader.readByte(buffer)#print("questype = {0}".format(self.questype))

        self.mapid = math.floor(reader.readDouble(buffer))#print("mapid = {0}".format(self.mapid))

        self.knownStepsListLen = reader.readUnsignedShort(buffer)#print("knownStepsListLen = {0}".format(self.knownStepsListLen))

        for x in range(0, self.knownStepsListLen):
            typeindice = reader.readUnsignedShort(buffer)
            direction = reader.readByte(buffer)
            indice = reader.readVarShort(buffer)
            liste = [typeindice,direction,indice]
            self.liste1.append(liste)
        #print(self.liste1)
        if(typeindice != 462):
            self.totalStepCount = reader.readByte(buffer)#print("totalStepCount = {0}".format(self.totalStepCount))

            self.checkPointCurrent = reader.readVarUhInt(buffer)#print("checkPointCurrent = {0}".format(self.checkPointCurrent))

            self.checkPointTotal = reader.readVarUhInt(buffer)#print("checkPointTotal = {0}".format(self.checkPointTotal))

            self.availableRetryCount = reader.readInt(buffer)#print("availableRetryCount = {0}".format(self.availableRetryCount))

            self.flagsLen = reader.readUnsignedShort(buffer)#print("flagsLen = {0}".format(self.flagsLen))

            for x in range(0, self.flagsLen):
                self.liste2.append(math.floor(reader.readDouble(buffer)))
                self.liste3.append(reader.readByte(buffer))
            #print("liste2 = {0}".format(self.liste2))
    def __repr__(self):
        
        liste.append(self.questype)
        liste.append(self.mapid)
        liste.append(self.knownStepsListLen)
        liste.append(self.liste1)
        liste.append(self.totalStepCount)
        liste.append(self.checkPointCurrent)
        liste.append(self.checkPointTotal)
        liste.append(self.availableRetryCount)
        liste.append(self.flagsLen)
        liste.append(self.liste2)
        liste.append(self.liste3)
        return liste