# node/persistence.py
import json
import os
from common.constants import STATE_FILE, INITIAL_STATE

def load_state():
    if not os.path.exists(STATE_FILE):
        return {
            "fsm_state": INITIAL_STATE,
            "last_seq": 0
        }

    try:
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    except Exception:
        # Corrupt state → fail safe
        return {
            "fsm_state": INITIAL_STATE,
            "last_seq": 0
        }

def save_state(state):
    temp_file = STATE_FILE + ".tmp"
    with open(temp_file, "w") as f:
        json.dump(state, f)
    os.replace(temp_file, STATE_FILE)
