import socket
import time

IP='0.0.0.0'
PORT=8081
ADDR=(IP, PORT)

pins = {1:0, 2:0, 3:0}

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(ADDR)
s.listen(5)

while True:
    conn, addr = s.accept()
    print("client: ", addr)
    data = conn.recv(3)

    if not data:
        print("client closed connection")
        conn.close()
        continue

    data = data.decode("UTF-8")
    
    print("Pin:", data[0])
    print("State:", data[2])
    
    conn.send(b"OK")
    conn.close()


