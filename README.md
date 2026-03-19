# Network Attack Simulation using Scapy

## Overview

This project demonstrates controlled simulation and analysis of two network attacks:

* **SYN Flood**
* **UDP Flood**

The simulations are implemented using **Python (Scapy)** in an isolated virtual lab to study packet-level behavior and impact on a target system.

---

## ⚠️ Disclaimer

This project is strictly for **educational purposes only**.
All simulations were performed in a controlled environment (**Kali Linux → Metasploitable**).

---

## Lab Configuration

### Virtual Machines

* **Attacker:** Kali Linux
* **Target:** Metasploitable

### Network Setup

* Adapter Type: **Host-Only Adapter**
* Both machines are on the same subnet

### IP Configuration

* Kali: `192.168.56.103`
* Metasploitable: `192.168.56.102`

---

## Environment Verification

### Connectivity Test

```bash
ping 192.168.56.102
```

<img width="590" height="65" alt="Ping Success" src="https://github.com/user-attachments/assets/411f4b28-fd0c-4c12-ba57-6e5e009a2387" />

---

### Target Service Setup

```bash
sudo /etc/init.d/apache2 start
```

Verify:

```bash
netstat -an | grep :80
```

<img width="757" height="198" alt="Apache Running" src="https://github.com/user-attachments/assets/81beefb4-64b5-45ae-a563-15052bf62ec3" />

---

## SYN Flood Simulation

### Execution

```bash
sudo python3 syn_demo.py
```

**Input:**

```
Target IP: 192.168.56.102
Port: 80
```

<img width="484" height="347" alt="SYN Script Output" src="https://github.com/user-attachments/assets/980e271d-acd6-4330-be8a-476c67e67227" />

---

### Monitoring

```bash
sudo tcpdump -i eth0 tcp
```

<img width="840" height="483" alt="SYN tcpdump Output" src="https://github.com/user-attachments/assets/9fbb1367-6660-4109-a32e-a4e665745a15" />

---

### 📦 Packet Capture & Transfer

Traffic was captured on the target using `tcpdump` and saved as a `.pcap` file:

```bash
sudo tcpdump -i eth0 tcp -w syn_capture.pcap
```

The file was then transferred to Kali using a local network transfer method (netcat) for further analysis.

---

### Result

* Multiple SYN packets observed
* SYN-ACK responses generated
* No final ACK → half-open connections

---

## UDP Flood Simulation

### Execution

```bash
sudo python3 udp_demo.py
```

**Input:**

```
Target IP: 192.168.56.102
```

<img width="459" height="240" alt="UDP Script Output" src="https://github.com/user-attachments/assets/0235d03e-ed58-4a99-aaa7-7190daf50f04" />

---

### Monitoring

```bash
sudo tcpdump -i eth0 udp
```

<img width="863" height="395" alt="UDP tcpdump Output" src="https://github.com/user-attachments/assets/ab8a52fb-57e3-47d3-adfe-0ea1f03ba81d" />

---

### 📦 Packet Capture & Transfer

UDP traffic was captured and stored:

```bash
sudo tcpdump -i eth0 udp -w udp_capture.pcap
```

The capture file was then transferred to Kali for analysis.

---

### Result

* Continuous UDP packets observed
* Random ports and payloads
* High traffic volume generated

---

## Wireshark Analysis

### SYN Flood Analysis

**Filter used:**

```
tcp.flags.syn == 1 && tcp.flags.ack == 0
```

Observations:

* Large number of SYN packets
* Same destination (`192.168.56.102:80`)
* Multiple random source IPs
* No corresponding ACK packets

<img width="1349" height="566" alt="Screenshot 2026-03-19 144620" src="https://github.com/user-attachments/assets/bdc23607-3211-49f0-b162-014fac985ca6" />


---

### UDP Flood Analysis

**Filter used:**

```
udp
```

Observations:

* Continuous UDP packet flow
* Random source and destination ports
* Consistent payload size (Len=128)
* High packet frequency

<img width="1169" height="593" alt="Screenshot 2026-03-19 144522" src="https://github.com/user-attachments/assets/e1f39da1-35db-4782-94a4-d38b0de0f4ef" />

---

## Key Observations

* TCP-based attacks exploit connection state (half-open connections)
* UDP-based attacks rely on high traffic volume
* Packet crafting enables controlled simulation and analysis

---

## Conclusion

This experiment demonstrates how network attacks behave at the packet level and highlights the importance of:

* Firewalls
* Intrusion Detection Systems (IDS)
* Traffic monitoring tools

---

## How to Run

```bash
pip install scapy
sudo python3 syn_demo.py
sudo python3 udp_demo.py
```

---

## Project Structure

```
.
├── syn_demo.py
├── udp_demo.py
├── screenshots/
└── README.md
```

---

## Author

**Abhinav Kumar Rai**

---
