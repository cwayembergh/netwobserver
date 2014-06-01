import socket

from datetime import datetime
from gatherer.models import *
from gatherer.log import logParser
from threading import Thread
from time import sleep

MAX_DATA_RECEIVED = 2000
PROBEPORT = 3874

def responder():
	try:
		#create the server socket
		serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		#bind the socket
		serversocket.bind(('0.0.0.0', PROBEPORT))
		serversocket.listen(5)

		running = True
		while running:
			#accept connections from outside
			(clientsocket, address) = serversocket.accept()
			Thread(target=handler, args=(clientsocket,)).start()
	except socket.error:
		pass



def handler(clientsocket):
	
	clientsocket.setblocking(0)
	clientsocket.settimeout(60)
	try:
		#print("[+] Connection established")
		# Phase 1 : Probe send its identity
		#identity = int.from_bytes(clientsocket.recv(4),byteorder='little') # identity of the probe
		identity = clientsocket.recv(18).decode() # identity of the probe (MAC address)
		#print("[+] Identity received: %s" % identity)
		clientsocket.send(b'1')

		## Phase 2 = Data receive
		dataSize = int.from_bytes(clientsocket.recv(4),byteorder='big')
		#print("[*] Size received (%s)" % dataSize)
		clientsocket.send(b'1')

		data = clientsocket.recv(min(dataSize,1024))

		while len(data) < dataSize :
			data += clientsocket.recv(1024)
		
		logParser.probeParser(data.decode())
		#print("%s" % data.decode())
		#print("[*] Connection closed.")
	except socket.timeout:
		pass

	except Exception as e:
		OperationalError(source='Probe Responder', error='%s' % e).save()

	finally:
		clientsocket.close()


if __name__ == '__main__':
	responder()