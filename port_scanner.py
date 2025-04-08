import socket
from datetime import datetime

def scan_ports(target, port_range=100):
    open_ports = []

    print(f"[+] Starting scan on {target}")
    for port in range(1, port_range + 1):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((target, port))
            if result == 0:
                try:
                    banner = s.recv(1024).decode().strip()
                except:
                    banner = "No banner"
                open_ports.append((port, banner))
                print(f"[OPEN] Port {port} - {banner}")
            s.close()
        except Exception as e:
            print(f"[-] Error on port {port}: {e}")
            continue

    return open_ports

if __name__ == "__main__":
    target = input("Enter IP or domain to scan: ").strip()
    port_limit = input("Enter number of ports to scan (default 100): ").strip()

    if not target:
        print("[-] No target provided. Exiting.")
    else:
        port_range = int(port_limit) if port_limit.isdigit() else 100
        start_time = datetime.now()

        open_ports = scan_ports(target, port_range)

        # Save results
        filename = f"{target.replace('.', '_')}_ports.txt"
        with open(filename, "w") as f:
            f.write(f"# Port scan results for {target} on {start_time}\n\n")
            for port, banner in open_ports:
                f.write(f"Port {port}: {banner}\n")

        print(f"\n[✔] Scan complete. {len(open_ports)} open ports found.")
        print(f"[💾] Results saved to: {filename}")
