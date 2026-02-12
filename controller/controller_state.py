import json
import os
from common.constants import CONTROLLER_STATE_FILE, NODES

def load_controller_state():
    if not os.path.exists(CONTROLLER_STATE_FILE):
        return {node: 0 for node in NODES}

    try:
        with open(CONTROLLER_STATE_FILE, "r") as f:
            return json.load(f)
    except Exception:
        # Corrupt state → reset safely
        return {node: 0 for node in NODES}

def save_controller_state(state):
    temp_file = CONTROLLER_STATE_FILE + ".tmp"
    with open(temp_file, "w") as f:
        json.dump(state, f)
    os.replace(temp_file, CONTROLLER_STATE_FILE)
