import json
import os
from common.constants import INITIAL_STATE

def load_state(state_file):
    if not os.path.exists(state_file):
        return {
            "fsm_state": INITIAL_STATE,
            "last_seq": 0
        }

    try:
        with open(state_file, "r") as f:
            return json.load(f)
    except Exception:
        return {
            "fsm_state": INITIAL_STATE,
            "last_seq": 0
        }

def save_state(state, state_file):
    temp_file = state_file + ".tmp"
    with open(temp_file, "w") as f:
        json.dump(state, f)
    os.replace(temp_file, state_file)
