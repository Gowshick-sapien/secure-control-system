# common/constants.py

CONTROLLER_ADDR = ("127.0.0.1", 9001)

NODES = {
    "AVIONICS": ("127.0.0.1", 9000),
    "PAYLOAD": ("127.0.0.1", 9002),
    "RECOVERY": ("127.0.0.1", 9003),
    "PROPULSION": ("127.0.0.1", 9004),
}

STATE_DIR = "storage/"
INITIAL_STATE = "SAFE"
