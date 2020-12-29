import socket
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

ESP8266_ADDR = ("192.168.43.246", 8081)

#output digital device 
devices = {1:0, 2:0, 3:0}

def set_device_state(_id, state):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect(ESP8266_ADDR)
        payload = b"%d:%d"%(_id,state)
        s.send(payload)
        data = s.recv(1024)
        data = data.decode("UTF-8")
        s.close()
        print(data)
        if data == "OK":
            return True
    except Exception as e:
        print(e)
    return False

@app.route("/", methods=["GET", "POST"])
def index():
    devs = {"devices":[{"id":k,"state":v} for k,v in devices.items()]}
    print(devs)
    return render_template("index.html", **devs)

@app.route("/devices/<int:id>/<int:state>", methods=["GET"])
def dev_view(id, state):
    print(id, state)
    if id not in devices.keys():
        return jsonify({"msg":"device not found"}), 400
    if state not in [0,1]:
        return jsonify({"msg":"invalid state"}), 400
    if devices[id] == state:
        return jsonify({"msg":"OK"}), 200
    if set_device_state(id, state):
        devices[id] = state
        return jsonify({"msg":"OK"}), 200
    return jsonify({"msg":"unable to set device state"}), 500


if __name__ == "__main__":
    #set all devices to an intial state
    for dev, state in devices.items():
        set_device_state(dev, state)
    app.run("0.0.0.0", 5000, debug=True)
