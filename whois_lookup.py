import sys
import subprocess
from datetime import datetime

# Try to import 'whois', install if not available
try:
    import whois
except ImportError:
    print("[*] 'python-whois' not found. Installing now...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "python-whois"])
    import whois

def lookup_whois(query):
    try:
        w = whois.whois(query)
        return w
    except Exception as e:
        print(f"[-] Error: {e}")
        return None

if __name__ == "__main__":
    query = input("Enter domain or IP for WHOIS lookup: ").strip()

    if not query:
        print("[-] No input provided. Exiting.")
    else:
        print(f"\n[+] Performing WHOIS lookup on {query}...\n")
        result = lookup_whois(query)

        if result:
            result_str = ""
            for key, value in result.items():
                result_str += f"{key}: {value}\n"

            print(result_str)

            filename = f"{query.replace('.', '_')}_whois.txt"
            with open(filename, "w") as f:
                f.write(f"# WHOIS data for {query} - {datetime.now()}\n\n")
                f.write(result_str)

            print(f"\n[✔] WHOIS info saved to: {filename}")
        else:
            print("[-] No WHOIS data found.")
