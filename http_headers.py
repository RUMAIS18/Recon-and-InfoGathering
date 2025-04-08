import sys
import subprocess
from datetime import datetime

# Auto-install requests if not available
try:
    import requests
except ImportError:
    print("[*] 'requests' not found. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests

def fetch_headers(url):
    try:
        if not url.startswith("http"):
            url = "http://" + url
        response = requests.get(url, timeout=5)
        return response.headers
    except Exception as e:
        return {"Error": str(e)}

if __name__ == "__main__":
    target = input("Enter domain or URL: ").strip()

    if not target:
        print("[-] No target provided. Exiting.")
    else:
        headers = fetch_headers(target)
        filename = f"{target.replace('.', '_').replace('http://', '').replace('https://', '')}_headers.txt"

        print(f"\n[+] Headers for {target}:\n")
        with open(filename, "w") as f:
            f.write(f"# HTTP Headers for {target} - {datetime.now()}\n\n")
            for key, value in headers.items():
                print(f"{key}: {value}")
                f.write(f"{key}: {value}\n")

        print(f"\n[✔] Headers saved to: {filename}")
