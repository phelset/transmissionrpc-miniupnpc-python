# -*- coding: utf-8 -*-
# wrapperclass

import transmissionrpc

class Transmission:
	def __init__(self, address, port):
		self.client = transmissionrpc.Client(address, port)
		self.session = self.client.get_session()

	def getPeerPort(self):
		return self.session.peer_port

	def setPeerPort(self, port):
		self.session.peer_port = port
