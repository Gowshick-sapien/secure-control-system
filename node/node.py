import socket
import os
import sys

from common.constants import NODES, INITIAL_STATE, STATE_DIR
from common.packet import parse_packet
from node.persistence import load_state, save_state

def main(node_name):

    addr = NODES[node_name]
    state_file = f"{STATE_DIR}{node_name.lower()}_state.json"

    state = load_state(state_file)
    print(f"[BOOT:{node_name}] State={state['fsm_state']}, last_seq={state['last_seq']}")

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(addr)

    print(f"[{node_name}] Listening on {addr}")

    while True:
        data, _ = sock.recvfrom(4096)
        pkt = parse_packet(data)

        if pkt["target"] != node_name:
            continue  # ignore packets not for this node

        seq = pkt["seq"]
        payload = pkt["payload"]

        print(f"[{node_name}] RX seq={seq}, payload={payload}")

        if payload == "CRASH":
            print(f"[{node_name}] Simulated crash!")
            os._exit(1)

        state["fsm_state"] = payload
        state["last_seq"] = seq
        save_state(state, state_file)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python -m node.node <NODE_NAME>")
        sys.exit(1)

    main(sys.argv[1])
