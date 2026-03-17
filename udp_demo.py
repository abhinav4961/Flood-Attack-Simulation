# udp_demo.py
# UDP packet simulation using Scapy (lab use only)

from scapy.all import IP, UDP, Raw, send
import random
import string
import time


def generate_payload(size=128):
    """
    Create random data payload
    """
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(size))


def create_udp_packet(target_ip):
    """
    Build UDP packet with random source IP and ports
    """
    src_ip = ".".join(str(random.randint(1, 254)) for _ in range(4))
    src_port = random.randint(1024, 65535)
    dst_port = random.randint(1, 65535)

    payload = generate_payload()

    packet = IP(src=src_ip, dst=target_ip) / \
             UDP(sport=src_port, dport=dst_port) / \
             Raw(load=payload)

    return packet


def udp_simulation(target_ip, total_packets=200, delay=0.02):
    """
    Send UDP packets in controlled manner
    """
    print(f"\n[+] Starting UDP simulation → {target_ip}")

    sent = 0

    for i in range(total_packets):
        pkt = create_udp_packet(target_ip)
        send(pkt, verbose=False)

        sent += 1

        if sent % 40 == 0:
            print(f"[INFO] Sent {sent} packets")

        time.sleep(delay)

    print(f"\n[✓] Done. Total UDP packets sent: {sent}")


if __name__ == "__main__":
    target = input("Enter target IP: ")
    udp_simulation(target)
