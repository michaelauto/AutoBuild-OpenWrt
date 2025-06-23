import requests

url = "https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/direct.txt"
response = requests.get(url)
lines = response.text.splitlines()

domains = []
for line in lines:
    if line.startswith("  - '") and line.endswith("'"):
        domain = line[5:-1]  # 提取域名
        # 将 '+.' 替换为 '*.' 以适配 Shadowrocket 的通配符格式
        if domain.startswith('+.'):
            domain = '*.' + domain[2:]
        domains.append(domain)

with open("always_real_ip.conf", "w") as f:
    f.write("[General]\n")
    f.write(f"always-real-ip = {','.join(domains)}\n")