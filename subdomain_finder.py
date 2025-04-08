import requests
from datetime import datetime

def find_subdomains(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print("[-] Failed to fetch data from crt.sh")
            return []

        data = response.json()
        subdomains = set()
        for entry in data:
            name_value = entry['name_value']
            for sub in name_value.split('\n'):
                if sub.endswith(domain):
                    subdomains.add(sub.strip())
        return sorted(subdomains)

    except Exception as e:
        print(f"[-] Error: {e}")
        return []

if __name__ == "__main__":
    domain = input("Enter the domain name (example.com): ").strip()

    if not domain:
        print("[-] No domain entered. Exiting.")
    else:
        print(f"\n[+] Finding subdomains for {domain}...\n")
        subs = find_subdomains(domain)

        if subs:
            print(f"[+] Found {len(subs)} subdomains:\n")
            for s in subs:
                print(f"- {s}")

            # Save to file
            filename = f"{domain.replace('.', '_')}_subdomains.txt"
            with open(filename, 'w') as f:
                f.write(f"# Subdomains found for {domain} on {datetime.now()}\n\n")
                for s in subs:
                    f.write(s + "\n")

            print(f"\n[✔] Subdomains saved to: {filename}")
        else:
            print("[-] No subdomains found or error occurred.")
