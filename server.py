from fileinput import filename
from ipaddress import ip_address
import socket

s = socket.socket()
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

port = 8080
print(hostname, ip_address)
s.bind((ip_address, port))
s.listen(1)


print("Waiting for incoming connections")

conn, addr = s.accept()
print(addr, "Has connected")

filename = input("Enter File Name: ")
file = open(filename, 'rb')
file_data = file.read(1024)
file.close()
conn.send(file_data)
print("data is sent")