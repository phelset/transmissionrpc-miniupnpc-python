# -*- coding: utf-8 -*-

import miniupnpc

class UPnP:
	def __init__(self):
		self.upnp = miniupnpc.UPnP()
		self.upnp.discoverdelay = 200;

		# discover upnp igd
		print 'Discovering UPnP IGDs...'
		self.upnp.discover()

		# select an igd
		try:
			self.upnp.selectigd()
		except Exception, e:
			print 'Exception: %s' % e
			exit(1)

		# display information about the IGD and the internet connection
		print 'Local IP address: %s' % self.upnp.lanaddr
		print 'External IP address: %s' % self.upnp.externalipaddress()

	# methods to get mapping info

	def getPortMapping(self, port, protocol):
		return self.upnp.getspecificportmapping(port, protocol)

	def getFreePort(self, startPort, protocol):
		while self.getPortMapping(startPort, protocol) != None:
			return self.getFreePort(startPort + 1, protocol)
		return startPort

	# methods to check mapping

	def isPortMapped(self, port, protocol):
		return self.getPortMapping(port, protocol) == None

	def isPortMappedToIp(self, port, protocol, ip):
		portMapping = self.getPortMapping(port, protocol)
		if portMapping == None:
			return False
		else:
			(mappedIp, mappedPort, desc, c, d) = portMapping
			return mappedIp == ip

	# methods to manipulate igd

	def addPortMapping(self, port, protocol, ip):
		return self.upnp.addportmapping(port, protocol, ip, port, 'miniupnpc python', '')

	def deletePortMapping(self, port, protocol):
		return self.upnp.deleteportmapping(port, protocol)

	# methods using lanaddr as ip

	def isPortMappedToLanIp(self, port, protocol):
		return self.isPortMappedToIp(port, protocol, self.upnp.lanaddr)

	def addPortMappingToLanIp(self, port, protocol):
		return self.addPortMapping(port, protocol, self.upnp.lanaddr)
