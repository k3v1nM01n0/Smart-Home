import socket
import time

SERVER_IP='127.0.0.1'
PORT=8081
ADDR=(SERVER_IP, PORT)

pins = {1:0, 2:0, 3:0}



while True:
    # try:
        for pin , state in pins.items():
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(ADDR)
            pins[pin] = not state
            payload = b"%d:%d"%(pin, pins[pin])

            s.send(payload)
            data = s.recv(1024)
            print(data)

            s.close()
        time.sleep(2)

    # except Exception as e:
    #     print(e)
