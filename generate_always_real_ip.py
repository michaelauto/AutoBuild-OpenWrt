import requests

url = "https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/direct.txt"
response = requests.get(url)
lines = response.text.splitlines()

domains = []
for line in lines:
    if line.startswith("  - '") and line.endswith("'"):
        domain = line[5:-1]
        domains.append(domain)

with open("always_real_ip.conf", "w") as f:
    f.write("[General]\n")
    f.write(f"always-real-ip = {','.join(domains)}\n")