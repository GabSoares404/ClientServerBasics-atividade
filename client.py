from socket  import *
from constCS import *

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT)) # connect to server (block until accepted)
print(f"Connected to server {HOST}:{PORT}")

# Request 1: UPPER
request1 = f"{OP_UPPERCASE} ola mundo"
print(f"Sending: {request1}")
s.send(str.encode(request1))
response1 = s.recv(1024)
print(f"Response from server: {bytes.decode(response1)}\n")

# Request 2: REVERSE
request2 = f"{OP_REVERSE} ola mundo"
print(f"Sending: {request2}")
s.send(str.encode(request2))
response2 = s.recv(1024)
print(f"Response from server: {bytes.decode(response2)}\n")

s.close() # close the connection
