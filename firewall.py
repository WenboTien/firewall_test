import csv
from IPy import IP


"""
input: the string of the port range

output: The list consists of all qualified port number
"""
def port_range(port_str):
    if port_str.find('-') < 0:
        return [int(port_str)]
    port_list = port_str.split('-')
    return [i for i in range(int(port_list[0]), int(port_list[1]) + 1)]
    pass

"""
input: the string of the IP address range

output: The list consists of all qualified Ip address in Decimal
"""
def ip_range(ip_str):
    if ip_str.find('-') < 0:
        return [int(IP(ip_str).strDec())]
    ip_list = ip_str.split('-')
    return [i for i in range(int(IP(ip_list[0]).strDec()), int(IP(ip_list[1]).strDec()) + 1)]
    pass


class Firewall:
    """
    This is the Firewall constructor, I build a map to store the input:
    eg: {'inbound_tcp' : {80 : set('192.168.1.2', '192.168.1.3')}}
        {'outbound_udp' : {1000 : set('192.168.1.2', '192.168.1.3')}}
    """
    def __init__(self, csvPath):
        self.map = {}
        try:
            with open(csvPath, 'r') as csvFile:
                reader = csv.reader(csvFile)
                for row in reader:
                    direct_protocol = row[0] + '_' + row[1]
                    if direct_protocol not in self.map:
                        self.map[direct_protocol] = {}
                    for port in port_range(row[2]):
                        if port not in self.map[direct_protocol]:
                            self.map[direct_protocol][port] = set()
                        for ip in ip_range(row[3]):
                            self.map[direct_protocol][port].add(ip)
        except Exception as detail:
            print "This is the error ==> ", detail

    """
    This is the search function:
    (1)we check if the direction and protocol exists in the map,
    (2)than we check if the port number exists
    (3)after that, we check the ip_address information
    The Time Complexity : O(1)
    """
    def accept_packet(self, direction, protocol, port, ip_address):
        try:
            direct_protocol = direction + '_' + protocol
            if direct_protocol not in self.map:
                return False
            if port not in self.map[direct_protocol]:
                return False
            if int(IP(ip_address).strDec()) not in self.map[direct_protocol][port]:
                return False
            return True
        except Exception as detail:
            print "This is the error ==> ", detail
