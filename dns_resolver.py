import sys
import subprocess
from datetime import datetime

# Auto-install dnspython if not installed
try:
    import dns.resolver
except ImportError:
    print("[*] 'dnspython' not found. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "dnspython"])
    import dns.resolver

def resolve_records(domain):
    record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT']
    results = {}

    for rtype in record_types:
        try:
            answers = dns.resolver.resolve(domain, rtype)
            results[rtype] = [str(rdata) for rdata in answers]
        except Exception as e:
            results[rtype] = [f"Error: {e}"]

    return results

if __name__ == "__main__":
    domain = input("Enter domain to resolve DNS records: ").strip()

    if not domain:
        print("[-] No domain provided. Exiting.")
    else:
        print(f"[+] Resolving DNS records for {domain}...\n")
        records = resolve_records(domain)

        filename = f"{domain.replace('.', '_')}_dns_records.txt"
        with open(filename, "w") as f:
            f.write(f"# DNS records for {domain} - {datetime.now()}\n\n")
            for rtype, values in records.items():
                print(f"{rtype} Records:")
                f.write(f"{rtype} Records:\n")
                for value in values:
                    print(f" - {value}")
                    f.write(f" - {value}\n")
                print()
                f.write("\n")

        print(f"\n[✔] DNS records saved to: {filename}")
