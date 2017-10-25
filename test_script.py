from firewall import Firewall
import unittest


class TestFirewall(unittest.TestCase):
    def setUp(self):
        self.fw = Firewall('./fw.csv')

    def test_invalid_input(self):
        self.assertFalse(self.fw.accept_packet("inbound", "udp", 24, "-52.12.48.-92"))
        self.assertFalse(self.fw.accept_packet("inbound", "udp", "123", "52.12.48.92"))
        self.assertFalse(self.fw.accept_packet("inbound", "tcp_udp", 24, "52.12.48.92"))
        self.assertFalse(self.fw.accept_packet("in_out_inbound", "5", 24, "52.12.48.92"))

    def test_inbound_udp(self):
        self.assertTrue(self.fw.accept_packet("inbound",  "udp",  53,  "192.168.2.1"))
        self.assertFalse(self.fw.accept_packet("inbound",  "udp",  24,  "52.12.48.92"))

    def test_outbound_udp(self):
        self.assertTrue(self.fw.accept_packet("outbound", "udp", 1000, "52.12.48.92"))
        self.assertFalse(self.fw.accept_packet("outbound", "udp", 24, "52.12.48.92"))

    def test_inbound_tcp(self):
        self.assertTrue(self.fw.accept_packet("inbound", "tcp", 80, "192.168.1.2"))
        self.assertFalse(self.fw.accept_packet("inbound", "tcp", 24, "52.12.48.92"))

    def test_outbound_tcp(self):
        self.assertTrue(self.fw.accept_packet("outbound", "tcp", 10000, "192.168.10.11"))
        self.assertFalse(self.fw.accept_packet("outbound", "tcp", 24, "52.12.48.92"))

if __name__ == '__main__':
    unittest.main()
