import sys
import subprocess
import socket
import json
from datetime import datetime

# Auto-install requests
try:
    import requests
except ImportError:
    print("[*] 'requests' not found. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests

def resolve_to_ip(target):
    try:
        return socket.gethostbyname(target)
    except socket.gaierror:
        return None

def geo_lookup(ip):
    url = f"http://ip-api.com/json/{ip}"
    try:
        response = requests.get(url)
        return response.json()
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    target = input("Enter IP or domain for geolocation: ").strip()

    if not target:
        print("[-] No input provided. Exiting.")
    else:
        ip = resolve_to_ip(target)
        if not ip:
            print("[-] Invalid domain or IP.")
        else:
            print(f"[+] IP resolved: {ip}")
            geo_info = geo_lookup(ip)

            if geo_info.get("status") != "success":
                print(f"[-] Failed to get geolocation: {geo_info.get('message', geo_info.get('error'))}")
            else:
                filename = f"{ip.replace('.', '_')}_geo.txt"
                with open(filename, "w") as f:
                    f.write(f"# Geolocation info for {target} ({ip}) - {datetime.now()}\n\n")
                    for key, value in geo_info.items():
                        print(f"{key.capitalize()}: {value}")
                        f.write(f"{key.capitalize()}: {value}\n")

                print(f"\n[✔] Geolocation info saved to: {filename}")
