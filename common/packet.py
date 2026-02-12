# common/packet.py
import json

def build_packet(pkt_type, seq, target, payload):
    return json.dumps({
        "type": pkt_type,
        "seq": seq,
        "target": target,
        "payload": payload
    }).encode()

def parse_packet(raw_bytes):
    return json.loads(raw_bytes.decode())
