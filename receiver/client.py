import socket

s = socket.socket()

host = input("Enter host address: ")

port = 8080

s.connect((host, port))
print("connnected")

filename = input("Enter file name for incoming file:")
file = open(filename, 'wb')
file_data = s.recv(1024)
file.write(file_data)
file.close()

print("file is received")