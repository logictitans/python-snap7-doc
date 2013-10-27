import ctypes

S7Object = ctypes.c_uint
buffer_size = 65536
buffer_type = ctypes.c_ubyte * buffer_size
time_t = ctypes.c_uint64  # TODO: check if this is valid for all platforms
word = ctypes.c_uint16
longword = ctypes.c_uint32

# // PARAMS LIST
LocalPort       = 1
RemotePort      = 2
PingTimeout     = 3
SendTimeout     = 4
RecvTimeout     = 5
WorkInterval    = 6
SrcRef          = 7
DstRef          = 8
SrcTSap         = 9
PDURequest      = 10
MaxClients      = 11
BSendTimeout    = 12
BRecvTimeout    = 13
RecoveryTime    = 14
KeepAliveTime   = 15

# mask types
mkEvent = 0
mkLog = 1


# Area ID
S7AreaPE   = 0x81
S7AreaPA   = 0x82
S7AreaMK   = 0x83
S7AreaDB   = 0x84
S7AreaCT   = 0x1C
S7AreaTM   = 0x1D

# Word Length
S7WLBit     = 0x01
S7WLByte    = 0x02
S7WLWord    = 0x04
S7WLDWord   = 0x06
S7WLReal    = 0x08
S7WLCounter = 0x1C
S7WLTimer   = 0x1D

# Server Area ID  (use with Register/unregister - Lock/unlock Area)
# NOTE: these are not the same for the client!!
srvAreaPE = 0
srvAreaPA = 1
srvAreaMK = 2
srvAreaCT = 3
srvAreaTM = 4
srvAreaDB = 5

wordlen_to_ctypes = {
    S7WLByte: ctypes.c_int8,
    S7WLWord: ctypes.c_int16,
    S7WLDWord: ctypes.c_int32,
    S7WLReal: ctypes.c_int32,
    S7WLCounter: ctypes.c_int16,
    S7WLTimer: ctypes.c_int16,
}

block_types = {
    'OB': ctypes.c_int(0x38),
    'DB':  ctypes.c_int(0x41),
    'SDB': ctypes.c_int(0x42),
    'FC': ctypes.c_int(0x43),
    'SFC': ctypes.c_int(0x44),
    'FB': ctypes.c_int(0x45),
    'SFB': ctypes.c_int(0x46),
}

server_statuses = {
    0: 'SrvStopped',
    1: 'SrvRunning',
    2: 'SrvError',
}

cpu_statuses = {
    0: 'S7CpuStatusUnknown',
    4: 'S7CpuStatusStop',
    8: 'S7CpuStatusRun',
}


class SrvEvent(ctypes.Structure):
    _fields_ = [
        ('EvtTime', time_t),
        ('EvtSender', ctypes.c_int),
        ('EvtCode', longword),
        ('EvtRetCode', word),
        ('EvtParam1', word),
        ('EvtParam2', word),
        ('EvtParam3', word),
        ('EvtParam4', word),
    ]

    def __str__(self):
        return "<event time: %s sender: %s code: %s retcode: %s param1: " \
               "%s param2:%s param3: %s param4: " \
               "%s>" % (self.EvtTime, self.EvtSender, self.EvtCode,
                        self.EvtRetCode, self.EvtParam1, self.EvtParam2,
                        self.EvtParam3, self.EvtParam4)


class BlocksList(ctypes.Structure):
    _fields_ = [
        ('OBCount', ctypes.c_int32),
        ('FBCount', ctypes.c_int32),
        ('FCCount', ctypes.c_int32),
        ('SFBCount', ctypes.c_int32),
        ('SFCCount', ctypes.c_int32),
        ('DBCount', ctypes.c_int32),
        ('SDBCount', ctypes.c_int32),
    ]

    def __str__(self):
        return "<block list count OB: %s FB: %s FC: %s SFB: %x SFC: %s DB: %s" \
               " SDB: %s>" % (self.OBCount, self.FBCount, self.FCCount,
                             self.SFBCount, self.SFCCount, self.DBCount,
                             self.SDBCount)
