import sys
from Tkinter import Tk
from Client import Client

if __name__ == "__main__":
	try:
		serverAddr = '192.168.0.10'
		serverPort = 1025
		rtpPort = 65000
		fileName = 'movie.Mjpeg'	
	except:
		print "[Usage: ClientLauncher.py Server_name Server_port RTP_port Video_file]\n"	
	
	root = Tk()
	
	# Create a new client
	app = Client(root, serverAddr, serverPort, rtpPort, fileName)
	app.master.title("RTPClient")
	app.setupMovie()
	root.mainloop()
	
