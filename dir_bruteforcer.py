import sys
import subprocess
from datetime import datetime

# Auto-install requests
try:
    import requests
except ImportError:
    print("[*] Installing 'requests'...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests

def brute_force_dirs(base_url, wordlist_file):
    if not base_url.startswith("http"):
        base_url = "http://" + base_url

    valid_paths = []

    try:
        with open(wordlist_file, "r") as file:
            words = file.read().splitlines()
    except FileNotFoundError:
        print(f"[-] Wordlist '{wordlist_file}' not found.")
        return

    print(f"\n[+] Starting brute force on {base_url}...\n")
    for word in words:
        url = f"{base_url.rstrip('/')}/{word}"
        try:
            response = requests.get(url, timeout=3)
            if response.status_code in [200, 301, 302, 403]:
                print(f"[{response.status_code}] {url}")
                valid_paths.append(f"[{response.status_code}] {url}")
        except requests.RequestException:
            continue

    output_file = f"{base_url.replace('http://', '').replace('https://', '').replace('.', '_')}_dirs.txt"
    with open(output_file, "w") as f:
        f.write(f"# Found directories on {base_url} - {datetime.now()}\n\n")
        for path in valid_paths:
            f.write(path + "\n")

    print(f"\n[✔] Results saved to: {output_file}")

if __name__ == "__main__":
    target = input("Enter domain or URL: ").strip()
    wordlist = "wordlist.txt"
    if not target:
        print("[-] No input provided.")
    else:
        brute_force_dirs(target, wordlist)
