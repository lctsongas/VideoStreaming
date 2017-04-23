# VideoStreaming
CE4390 Video Streaming

#4-Button UI Implementation (No extensions)
Instructions:
1) Run the Server.py with the RTSP port number as the first argument.
	Choose a random, unused port number between 1024-65534

2) The server listens for 20 seconds so the user will have time to setup the
	client. Run the ClientLauncher.py with the following arguments:
		argv[1] = server address (the computer running Server.py IP
					address. Most likely the computer you are using.)
		argv[2] = server port number make sure this one matches the one
					set in the Server.py
		argv[3] = RTP port number. Choose a different port number 
					between 1024-65534 and do not choose the same port
					as the RTSP port.
		argv[4] = Set this to 'movie.Mjpeg' WITHOUT quotations

3) The client should be connected to the server now. If there are any
	errors, please ensure the following have been done:
		A) PIL library is installed (common error for us)
		B) IP address and port numbers are correct and not being used
		C) The server wait time did not timeout

4) Begin tseting the implementation by running through the validation
	scenario specified in the CE4390ExtensionValidation.pdf.

5) Once finished, close the Client and stop the server process. To see the
	statictics analysis, please refer to the StatiscticsAnalysis.pdf
		
	
	