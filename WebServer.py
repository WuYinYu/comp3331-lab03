import socket
import os
import sys
import datetime

if (len(sys.argv) != 2):
	print("Require Argument: Port")
	os._exit(0)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = (int)(sys.argv[1])
s.bind(('', port))
s.listen(1)
print("Server set up successfully")

#infinite loop
while True:
	#get request
	client_s, address = s.accept()
	sentence = client_s.recv(1024)
	#parse the request to determine the specific file being requested.
	message = sentence.split()
	require_message = message[1]
	temp = require_message.split("/")
	require_file = temp[1]
	print(require_file + "\n")
	try:
		# find file successfully
		# print("find file successfully")
		file = open(require_file, "r")

		# construct message to send
		out_message = file.read()
		response_header = "HTTP/1.1 200 OK\r\n"
		content_len = "Content-Length: " + str(len(out_message)) + "\r\n"

		# send message

		client_s.send(response_header)
		#print(response_header)
		client_s.send(content_len + "\r\n")
		#print(content_len)
		client_s.send(out_message)
		print(out_message)
		client_s.close()
	except IOError:
		error_response_header = "HTTP/1.1 404 Not Found\r\n"
		error_content = "<h1>Oops!</h1><h2>404 Not Found</h2>"
		client_s.send(error_response_header + "\r\n")
		client_s.send(error_content)
		client_s.close()