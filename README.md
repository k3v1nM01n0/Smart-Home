# Smart-Home

## Description
    Building a TCP server on ESP8266 to control its outputs.
    The board is programmed using platformio and the module used is WiFiClient.
    The interface used is Flask webserver that sends instructions to the to the TCP server. 

## Setup
    Install the platform io extension on VS IDE
    create new project and edit platformio.ini as folows:
    
    
        
        platform = espressif8266
        board = huzzah
        framework = arduino
        monitor_speed = 115200
       


### Requirements

    Esp8266 microcontroller
    Resisitor
    3 leds
    VS code with Platormio extension
    


## Running Server

Set the correct IP and Port of ESP8266 in [app.py](./server/app.py)

```python
ESP8266_ADDR = ("127.0.0.1", 8001)
```

Activate virtual and install requirements

```bash
cd server
python3 -m venv virtual
source virtual/bin/activate
pip install -r requirements.txt
```

Run development server

```bash
python app.py
```

**Note** The Web UI might show that a device has been successfully toggled even though there was an issue, in this case check the developer console on your browser, error checking will be added later.

You can also run the flask server against a test TCP server [here](./server/test_tcp_server.py)
