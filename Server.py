import sys, socket

from ServerWorkerv2 import ServerWorker

class Server:	
	
	def main(self):
		try:
			SERVER_PORT = 1025
		except:
			print "[Usage: Server.py Server_port]\n"
		rtspSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		rtspSocket.bind(('', SERVER_PORT))
		rtspSocket.listen(5)        

		# Receive client info (address,port) through RTSP/TCP session
		while True:
			clientInfo = {}
			clientInfo['rtspSocket'] = rtspSocket.accept()
			ServerWorker(clientInfo).run()		

if __name__ == "__main__":
	(Server()).main()


