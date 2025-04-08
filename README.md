 Tools Included

🔍 Subdomain Finder

    python subdomain_finder.py

📄 Whois Lookup

    python whois_lookup.py

🌐 DNS Resolver

    python dns_resolver.py

🛜 IP Lookup
    python port_scanner.py

🌍 IP Geolocation Finder

    python ip_geolocator.py

🧾 HTTP Header Grabber

        python http_headers.py

📂 Directory Bruteforcer

    python dir_bruteforcer.py

# Examples 
update the word list

Enter domain or IP for WHOIS lookup: example.com

[+] Performing WHOIS lookup on example.com...

domain_name: EXAMPLE.COM
registrar: RESERVED-INTERNET ASSIGNED NUMBERS AUTHORITY
creation_date: 1995-08-14 04:00:00
...

[✔] WHOIS info saved to: example_com_whois.txt



Enter IP or domain to scan: scanme.nmap.org
Enter number of ports to scan (default 100): 50

[OPEN] Port 22 - No banner
[OPEN] Port 80 - No banner

[✔] Scan complete. 2 open ports found.
[💾] Results saved to: scanme_nmap_org_ports.txt



Enter domain to resolve DNS records: google.com

A Records:
 - 142.250.77.14

NS Records:
 - ns1.google.com.
 - ns2.google.com.

...

[✔] DNS records saved to: google_com_dns_records.txt


Enter IP or domain for geolocation: google.com

[+] IP resolved: 142.250.77.206
Country: United States
RegionName: California
City: Mountain View
ISP: Google LLC
...

[✔] Geolocation info saved to: 142_250_77_206_geo.txt


Enter domain or URL: example.com

[+] Headers for example.com:

Content-Type: text/html
Date: Sun, 07 Apr 2025 19:10:43 GMT
Content-Encoding: gzip
Server: ECS (dfw/288D)
...

[✔] Headers saved to: example_com_headers.txt

Enter domain or URL: testphp.vulnweb.com

[200] http://testphp.vulnweb.com/admin
[301] http://testphp.vulnweb.com/uploads
[403] http://testphp.vulnweb.com/config

[✔] Results saved to: testphp_vulnweb_com_dirs.txt

