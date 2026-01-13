# node/node.py
import socket
import os

from common.constants import NODE_ADDR
from common.packet import parse_packet
from node.persistence import load_state, save_state

def main():
    state = load_state()
    print(f"[BOOT] State={state['fsm_state']}, last_seq={state['last_seq']}")

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(NODE_ADDR)

    print("[NODE] Listening on", NODE_ADDR)

    while True:
        data, addr = sock.recvfrom(4096)
        pkt = parse_packet(data)

        seq = pkt["seq"]
        payload = pkt["payload"]

        print(f"[RX] seq={seq}, payload={payload}")

        # CRASH injection
        if payload == "CRASH":
            print("[NODE] Simulated crash!")
            os._exit(1)

        # TEMP: accept everything
        state["fsm_state"] = payload  # placeholder
        state["last_seq"] = seq
        save_state(state)

if __name__ == "__main__":
    main()
