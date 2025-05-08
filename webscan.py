---

### **2. `webscan.py` (Python Script)**

```python
import requests
import sys
import socket

def check_headers(url):
    print(f"\n[+] Checking headers for {url}")
    try:
        r = requests.get(url)
        for h in ['Server', 'X-Frame-Options', 'X-XSS-Protection', 'Content-Security-Policy']:
            print(f"{h}: {r.headers.get(h, 'Missing')}")
    except:
        print("[-] Failed to fetch headers.")

def check_methods(url):
    print(f"\n[+] Checking HTTP methods for {url}")
    try:
        r = requests.options(url)
        print("Allowed Methods:", r.headers.get("Allow", "Unknown"))
    except:
        print("[-] Failed to check methods.")

def port_scan(host):
    print(f"\n[+] Basic Port Scan on {host}")
    ports = [21, 22, 80, 443, 8080]
    for port in ports:
        sock = socket.socket()
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Port {port}: OPEN")
        sock.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python webscan.py <URL>")
        sys.exit()

    url = sys.argv[1]
    hostname = url.replace("https://", "").replace("http://", "").split('/')[0]
    
    check_headers(url)
    check_methods(url)
    port_scan(hostname)