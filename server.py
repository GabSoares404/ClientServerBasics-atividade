from socket  import *
from constCS import *

def process_uppercase(text):
    return text.upper()

def process_reverse(text):
    return text[::-1]

s = socket(AF_INET, SOCK_STREAM) 
s.bind((HOST, PORT))
s.listen(1)
print(f"Server is listening on {HOST}:{PORT}...")

(conn, addr) = s.accept()
print(f"Connected by {addr}")

while True:
    data = conn.recv(1024)
    if not data: 
        break
    
    decoded_data = bytes.decode(data)
    print(f"Received from client: {decoded_data}")
    
    # Parse request
    parts = decoded_data.split(' ', 1)
    if len(parts) >= 2:
        command = parts[0]
        text_data = parts[1]
        
        # Process based on command
        if command == OP_UPPERCASE:
            response = process_uppercase(text_data)
        elif command == OP_REVERSE:
            response = process_reverse(text_data)
        else:
            response = "ERROR: Unknown command."
    else:
        response = "ERROR: Invalid format. Expected 'COMMAND data'."
        
    conn.send(str.encode(response))

conn.close()
