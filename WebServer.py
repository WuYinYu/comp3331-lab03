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
'''
from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)					# create socket for client
serverSocket.bind(('', serverPort))							# binds address (hostname, port numer) to socket
serverSocket.listen(1)											# Listen / wait for connections made to the socket
print "The server is ready to receive\n"						# Arg 1 = max no. queued connections

while 1:
	print "Ready to serve"
	connectionSocket, addr = serverSocket.accept()			# passively accepts TCP client connection
	# Receive and send client requests
	try:
		request = connectionSocket.recv(1024)				# receives get request from client

		message = request.split()[1];						# parse get request
		file_name = message.replace('/', '')					# remove slash
		print file_name, '\n'								

		file = open(file_name)								# open file
		http_output = file.read()							# read file, store as text / string
		connectionSocket.send('HTTP/1.1 200 OK\n\n')		# send HTTP header response
		connectionSocket.send(http_output)					# send HTTP text reponse
		connectionSocket.close()
	# IO Exception
	except IOError:
		connectionSocket.send('HTTP/1.1 404 File not found\n\n')
		connectionSocket.send('<h1><center>404 Error: File not found</center></h1>')
		connectionSocket.close()
'''
