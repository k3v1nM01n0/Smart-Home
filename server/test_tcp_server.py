'''
specs
------

client.send("id:state") //where id is a valid int between 1-3 and state is 1 or 0
- server.response("OK") //if success
- server.response("ERROR") //on error for examples invalid id
'''

import socket

HOST = "0.0.0.0"
PORT = 8000

ADDR= (HOST, PORT)

if __name__ == "__main__":
    pins = {1:0, 2:0, 3:0}
    sock_fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock_fd.bind(ADDR)

    sock_fd.listen(5)

    while True:
        conn, addr = sock_fd.accept()
        print("client connected", addr)

        data = conn.recv(3)
        if not data:
            conn.close()
            continue

        data = data.decode("UTF-8")
        id = int(data[0])
        state = int(data[2])
        if id not in state.keys() or state not in [1,0]:
            print("invalid pin or state")
            conn.send(b"ERROR")
            conn.close()
        
        pins[id] = state
        conn.send("OK")
        conn.close()




