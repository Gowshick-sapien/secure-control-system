import socket
from common.constants import CONTROLLER_ADDR, NODES
from common.packet import build_packet

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(CONTROLLER_ADDR)

    send_seq = 0

    print("[CTRL] Controller ready")
    print("Available nodes:", list(NODES.keys()))

    while True:
        raw = input("> ").strip().split()

        if len(raw) < 2:
            print("Usage: <NODE> <COMMAND>")
            continue

        node_name = raw[0].upper()
        command = raw[1]

        if node_name not in NODES:
            print("Unknown node")
            continue

        send_seq += 1
        pkt = build_packet("COMMAND", send_seq, node_name, command)

        sock.sendto(pkt, NODES[node_name])
        print(f"[TX] seq={send_seq} → {node_name}: {command}")

if __name__ == "__main__":
    main()
