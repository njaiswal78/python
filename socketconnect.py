import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('data.pr4e.org',80))
cmd='GET /intro-short.txt HTTP/1.0\r\nHost: data.pr4e.org\r\n\r\n'.encode()
s.send(cmd)

while True:
	data=s.recv(5000)
	if (len(data)<1):
		break
	print(data.decode('utf-8').strip())
s.close()