# firewall_test
This is python code for Firewall class

Dependencies: Python 2.7 (packages: csv, IPy)

(1) Firewall class design:

In preprocess phase, I create a map to store 4 kinds of key-value:

eg: map = {'inbound_tcp':{}, 'outbound_tcp':{}, 'inbound_udp':{}, 'outbound_udp':{} }

For each of them I create a sub key-value to store the relationship between port and ip address:

eg: 'inbound_tcp':{ 80 : set('192.168.1.2', '192.168.1.3'), 90 : set('192.168.1.2', '192.168.1.3')}

The disadvantage is this will waste spaces, but for searching process, it is really quick.

(2) Testing method:

I use unit test in python, I tesed the invalid input, inbound_tcp, outbound_tcp, and outbound_udp to cover different combinations.

I also tested the Boundary case of IP address and Port Number.

(3) Optimization:

If I have more time, and we're not satisfied with the preprocessing time, we can use tree structure to store the range, but the searching time would become O(logN)

(4) Team preference:

I would like to choose the data team, because I'm interested in the data visualizaion, data science and distributed system.
