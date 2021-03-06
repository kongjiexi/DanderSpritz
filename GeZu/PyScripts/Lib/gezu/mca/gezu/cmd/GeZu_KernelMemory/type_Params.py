# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *

class Params:

    def __init__(self):
        self.__dict__['baseAddress'] = 0
        self.__dict__['size'] = 0

    def __getattr__(self, name):
        if name == 'baseAddress':
            return self.__dict__['baseAddress']
        if name == 'size':
            return self.__dict__['size']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'baseAddress':
            self.__dict__['baseAddress'] = value
        elif name == 'size':
            self.__dict__['size'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU64(MSG_KEY_PARAMS_BASE_ADDRESS, self.__dict__['baseAddress'])
        submsg.AddU32(MSG_KEY_PARAMS_SIZE, self.__dict__['size'])
        mmsg.AddMessage(MSG_KEY_PARAMS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['baseAddress'] = submsg.FindU64(MSG_KEY_PARAMS_BASE_ADDRESS)
        self.__dict__['size'] = submsg.FindU32(MSG_KEY_PARAMS_SIZE)