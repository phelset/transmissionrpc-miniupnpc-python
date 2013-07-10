#!/usr/bin/env python
from transmission import Transmission
from upnp import UPnP

t = Transmission('localhost', 9091)
u = UPnP()

proto = 'UDP'
if u.isPortMapped(t.peer_port, proto):
	if not u.isPortMappedToLanIp(t.peer_port, proto):
		t.peer_port = u.getFreePort(t.peer_port, proto)
		u.addPortMappingToLanIp(t.peer_port, proto)
else:
	u.addPortMappingToLanIp(t.peer_port, proto)

print 'Transmission peer port is %s. The port is mapped in UPnP IGD.' % t.peer_port
exit(0)
