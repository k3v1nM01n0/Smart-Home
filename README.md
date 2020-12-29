## Description

TODO
## Setup

TODO

### Requirements

TODO

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