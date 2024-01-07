import psutil

print(psutil.net_io_counters())
# snetio(bytes_sent=557218884, bytes_recv=2467954712, packets_sent=2220295, packets_recv=3340639, errin=0, errout=0, dropin=0, dropout=0)

# print(psutil.net_connections())
# [sconn(fd=118, family=2, type=1, laddr=addr(ip=’192.168.12.184′, port=59666), raddr=addr(ip=’172.217.166.42′, port=443), status=’ESTABLISHED’, pid=2428), 
# sconn(fd=-1, family=2, type=2, laddr=addr(ip=’0.0.0.0′, port=631), raddr=(), status=’NONE’, pid=None), 
# sconn(fd=-1, family=2, type=1, laddr=addr(ip=’127.0.0.1′, port=3306), raddr=(), status=’LISTEN’, pid=None), 
# sconn(fd=145, family=2, type=1, laddr=addr(ip=’192.168.12.184′, port=56568), raddr=addr(ip=’172.217.166.35′, port=443), status=’ESTABLISHED’, pid=2428), 
# sconn(fd=-1, family=2, type=2, laddr=addr(ip=’0.0.0.0′, port=52253), raddr=(), status=’NONE’, pid=None)] 


print(psutil.net_if_addrs())
# {'Ethernet 4': [snicaddr(family=<AddressFamily.AF_LINK: -1>, address='00-FF-7B-92-D5-DA', netmask=None, broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET: 2>, address='10.4.2.1', netmask='255.255.255.0', broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET: 2>, address='169.254.107.122', netmask='255.255.0.0', broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET6: 23>, address='fe80::789a:90ff:476a:6b7a', netmask=None, broadcast=None, ptp=None)], 'Ethernet': [snicaddr(family=<AddressFamily.AF_LINK: -1>, address='0A-E0-AF-A1-00-30', netmask=None, broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET: 2>, address='192.168.5.102', netmask='255.255.255.0', broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET6: 23>, address='fe80::298d:422a:90e6:879f', netmask=None, broadcast=None, ptp=None)], 'Loopback Pseudo-Interface 1': [snicaddr(family=<AddressFamily.AF_INET: 2>, address='127.0.0.1', netmask='255.0.0.0', broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_INET6: 23>, address='::1', netmask=None, broadcast=None, ptp=None)]}