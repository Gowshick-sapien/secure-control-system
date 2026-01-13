# common/packet.py
import json

def build_packet(pkt_type, seq, payload):
    return json.dumps({
        "type": pkt_type,
        "seq": seq,
        "payload": payload
    }).encode()

def parse_packet(raw_bytes):
    return json.loads(raw_bytes.decode())
