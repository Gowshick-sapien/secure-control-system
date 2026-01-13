# controller/controller.py
import socket

from common.constants import CONTROLLER_ADDR, NODE_ADDR
from common.packet import build_packet

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(CONTROLLER_ADDR)

    send_seq = 0
    print("[CTRL] Controller ready")

    while True:
        cmd = input("> send ").strip()
        send_seq += 1

        pkt = build_packet("COMMAND", send_seq, cmd)
        sock.sendto(pkt, NODE_ADDR)

        print(f"[TX] seq={send_seq}, payload={cmd}")

if __name__ == "__main__":
    main()
