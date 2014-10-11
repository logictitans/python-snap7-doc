import unittest
import logging
import snap7
from snap7.snap7exceptions import Snap7Exception


logging.basicConfig(level=logging.WARNING)

ip = '127.0.0.1'
tcpport = 1102
db_number = 1
rack = 1
slot = 1


class TestClient(unittest.TestCase):

    def setUp(self):
        self.client = snap7.client.Client()
        self.client.connect(ip, rack, slot, tcpport)

    def tearDown(self):
        self.client.disconnect()
        self.client.destroy()

    def test_db_read(self):
        size = 40
        start = 0
        db = 1
        data = bytearray(40)
        self.client.db_write(db_number=db, start=start, data=data)
        result = self.client.db_read(db_number=db, start=start, size=size)
        self.assertEqual(data, result)

    def test_db_write(self):
        size = 40
        data = bytearray(size)
        self.client.db_write(db_number=1, start=0, data=data)

    def test_db_get(self):
        self.client.db_get(db_number=db_number)

    def test_upload(self):
        """
        this raises an exception due to missing authorization? maybe not
        implemented in server emulator
        """
        self.assertRaises(Snap7Exception, self.client.upload, db_number)

    @unittest.skip("TODO: invalid block size")
    def test_download(self):
        data = bytearray(1024)
        self.client.download(block_num=db_number, data=data)

    def test_read_area(self):
        area = snap7.snap7types.areas.DB
        dbnumber = 1
        amount = 1
        start = 1
        self.client.read_area(area, dbnumber, start, amount)

    def test_write_area(self):
        area = snap7.snap7types.areas.DB
        dbnumber = 1
        size = 1
        start = 1
        data = bytearray(size)
        self.client.write_area(area, dbnumber, start, data)

    def test_list_blocks(self):
        blockList = self.client.list_blocks()

    def test_list_blocks_of_type(self):
        self.client.list_blocks_of_type(snap7.snap7types.block_types['DB'], 10)

    def test_set_session_password(self):
        password = 'abcdefgh'
        self.client.set_session_password(password)

    def test_clear_session_password(self):
        self.client.clear_session_password()

    def test_set_connection_params(self):
        self.client.set_connection_params("10.0.0.2", 10, 10)

    def test_set_connection_type(self):
        self.client.set_connection_type(1)
        self.client.set_connection_type(2)
        self.client.set_connection_type(3)
        self.client.set_connection_type(20)

    def test_get_connected(self):
        self.client.get_connected()

    @unittest.skip("TODO: item not available?")
    def test_ab_read(self):
        start = 1
        size = 1
        data = bytearray(size)
        self.client.ab_write(start=start, data=data)
        self.client.ab_read(start=start, size=size)

    @unittest.skip("TODO: crash client: FATAL: exception not rethrown")
    def test_ab_write(self):
        start = 1
        size = 10
        data = bytearray(size)
        self.client.ab_write(start=start, data=data)

    @unittest.skip("TODO: crash client: FATAL: exception not rethrown")
    def test_as_ab_read(self):
        start = 1
        size = 1
        self.client.as_ab_read(start=start, size=size)

    @unittest.skip("TODO: not yet fully implemented")
    def test_as_ab_write(self):
        start = 1
        size = 10
        data = bytearray(size)
        self.client.as_ab_write(start=start, data=data)

    def test_compress(self):
        time = 1000
        self.client.compress(time)

    def test_as_compress(self):
        time = 1000
        self.client.as_compress(time)

    def test_set_param(self):
        values = (
            (snap7.snap7types.PingTimeout, 800),
            (snap7.snap7types.SendTimeout, 15),
            (snap7.snap7types.RecvTimeout, 3500),
            (snap7.snap7types.SrcRef, 128),
            (snap7.snap7types.DstRef, 128),
            (snap7.snap7types.SrcTSap, 128),
            (snap7.snap7types.PDURequest, 470),
        )
        for param, value in values:
            self.client.set_param(param, value)

        self.assertRaises(Exception, self.client.set_param,
                          snap7.snap7types.RemotePort, 1)

    def test_get_param(self):
        expected = (
            (snap7.snap7types.RemotePort, tcpport),
            (snap7.snap7types.PingTimeout, 750),
            (snap7.snap7types.SendTimeout, 10),
            (snap7.snap7types.RecvTimeout, 3000),
            (snap7.snap7types.SrcRef, 256),
            (snap7.snap7types.DstRef, 0),
            (snap7.snap7types.SrcTSap, 256),
            (snap7.snap7types.PDURequest, 480),
        )
        for param, value in expected:
            self.assertEqual(self.client.get_param(param), value)

        non_client = snap7.snap7types.LocalPort, snap7.snap7types.WorkInterval,\
                     snap7.snap7types.MaxClients, snap7.snap7types.BSendTimeout,\
                     snap7.snap7types.BRecvTimeout, snap7.snap7types.RecoveryTime,\
                     snap7.snap7types.KeepAliveTime

        # invalid param for client
        for param in non_client:
            self.assertRaises(Exception, self.client.get_param,  non_client)

    @unittest.skip("TODO: not yet fully implemented")
    def test_as_copy_ram_to_rom(self):
        self.client.copy_ram_to_rom()

    @unittest.skip("TODO: not yet fully implemented")
    def test_as_ct_read(self):
        self.client.as_ct_read()

    @unittest.skip("TODO: not yet fully implemented")
    def test_as_ct_write(self):
        self.client.as_ct_write()

    @unittest.skip("TODO: not yet fully implemented")
    def test_as_db_fill(self):
        self.client.as_db_fill()

    def test_as_db_get(self):
        self.client.db_get(db_number=db_number)

    @unittest.skip("TODO: crash client: FATAL: exception not rethrown")
    def test_as_db_read(self):
        size = 40
        start = 0
        db = 1
        data = bytearray(40)
        self.client.db_write(db_number=db, start=start, data=data)
        result = self.client.as_db_read(db_number=db, start=start, size=size)
        self.assertEqual(data, result)

    @unittest.skip("TODO: crash client: FATAL: exception not rethrown")
    def test_as_db_write(self):
        size = 40
        data = bytearray(size)
        self.client.as_db_write(db_number=1, start=0, data=data)

    def test_as_download(self):
        data = bytearray(128)
        self.client.as_download(block_num=-1, data=data)

    def test_plc_stop(self):
        self.client.plc_stop()

    def test_plc_hot_start(self):
        self.client.plc_hot_start()

    def test_plc_cold_start(self):
        self.client.plc_cold_start()


class TestClientBeforeConnect(unittest.TestCase):
    """
    Test suite of items that should run without an open connection.
    """
    def setUp(self):
        self.client = snap7.client.Client()

    def test_set_param(self):
        values = (
            (snap7.snap7types.RemotePort, 1102),
            (snap7.snap7types.PingTimeout, 800),
            (snap7.snap7types.SendTimeout, 15),
            (snap7.snap7types.RecvTimeout, 3500),
            (snap7.snap7types.SrcRef, 128),
            (snap7.snap7types.DstRef, 128),
            (snap7.snap7types.SrcTSap, 128),
            (snap7.snap7types.PDURequest, 470),
        )
        for param, value in values:
            self.client.set_param(param, value)


if __name__ == '__main__':
    unittest.main()


# TODO: implement
"""
Cli_AsEBRead
Cli_AsEBWrite
Cli_AsFullUpload
Cli_AsListBlocksOfType
Cli_AsMBRead
Cli_AsMBWrite
Cli_AsReadArea
Cli_AsReadSZL
Cli_AsReadSZLList
Cli_AsTMRead
Cli_AsTMWrite
Cli_AsUpload
Cli_AsWriteArea
Cli_CheckAsCompletion
Cli_Connect
Cli_CopyRamToRom
Cli_CTRead
Cli_CTWrite
Cli_DBFill
Cli_Delete
Cli_EBRead
Cli_EBWrite
Cli_ErrorText
Cli_FullUpload
Cli_GetAgBlockInfo
Cli_GetCpInfo
Cli_GetCpuInfo
Cli_GetExecTime
Cli_GetLastError
Cli_GetOrderCode
Cli_GetParam
Cli_GetPduLength
Cli_GetPgBlockInfo
Cli_GetPlcDateTime
Cli_GetPlcStatus
Cli_GetProtection
Cli_IsoExchangeBuffer
Cli_MBRead
Cli_MBWrite
Cli_ReadArea
Cli_ReadMultiVars
Cli_ReadSZL
Cli_ReadSZLList
Cli_SetAsCallback
Cli_SetParam
Cli_SetPlcDateTime
Cli_SetPlcSystemDateTime
Cli_SetSessionPassword
Cli_TMRead
Cli_TMWrite
Cli_WaitAsCompletion
Cli_WriteMultiVars
"""
