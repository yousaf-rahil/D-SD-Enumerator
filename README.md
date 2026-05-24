# 🔍 D-SD Enumerator

> Two Python-based reconnaissance scripts for 
> DNS record enumeration and subdomain discovery.
> Built for ethical hacking, CTF challenges and 
> penetration testing practice.

![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Security](https://img.shields.io/badge/Topic-Reconnaissance-red?style=for-the-badge)
![Pentesting](https://img.shields.io/badge/Use-Ethical%20Hacking-darkgreen?style=for-the-badge)
![Threading](https://img.shields.io/badge/Feature-Multi--Threading-blue?style=for-the-badge)

> ⚠️ **Disclaimer:** This tool is built for 
> educational purposes and ethical hacking only.
> Always get proper authorization before testing
> any domain you do not own.

---

## 📌 What It Does

### 🔎 DNS Enumerator (`dns_enumerator.py`)
- Checks internet connectivity before running
- Queries multiple DNS record types
- Records fetched: **A, AAAA, CNAME, MX, TXT**
- Uses Google Public DNS (8.8.8.8) as resolver
- Displays results directly in terminal

### 🌐 Subdomain Enumerator (`subdomain_enumerator.py`)
- Uses **multi-threading** for fast discovery
- Reads from a subdomain wordlist
- Saves discovered subdomains to a `.txt` file
- Thread-safe file writing using **Lock()**
- Graceful Ctrl+C exit handling

---

## 🛠️ Requirements

```bash
pip install tqdm dnspython requests
```

---

## 🚀 How To Use

### DNS Enumerator
```bash
# Change target_domain variable on line 30
# then run:
python3 dns_enumerator.py
```

### Subdomain Enumerator
```bash
# Change target variable on line 17
# Make sure subdomains.txt is in same directory
python3 subdomain_enumerator.py
```

> ⚠️ Make sure `subdomains.txt` wordlist is in 
> the same directory as the script

---

## 📂 Project Structure

```
D-SD-Enumerator/
│
├── dns_enumerator.py        # DNS record enumeration
├── subdomain_enumerator.py  # Subdomain discovery
├── subdomains.txt           # Wordlist for subdomains
└── discovered_subdomains.txt # Output file (auto-created)
```

---

## 📄 Code Preview

### DNS Enumerator
```python
record_list = ['A', 'AAAA', 'CNAME', 'MX', 'TXT']
resolver = dns.resolver.Resolver()
resolver.nameservers = ['8.8.8.8']

for i in record_list:
    try:
        answer = resolver.resolve(target_domain, i)
        if answer.rrset:
            print(f"{i} records of {target_domain}")
            for data in answer.rrset:
                print(f"\t{data}")
    except dns.resolver.NoAnswer:
        continue
```

### Subdomain Enumerator
```python
def sub_domain(subdomains):
    url = f"http://{subdomains}.{target}"
    try:
        requests.get(url)
    except requests.ConnectionError:
        pass
    else:
        print(f"[+] Discovered: {url}")
        with lock:
            with open('discovered_subdomains.txt', 'a') as file:
                file.write(url + '\n')

# Threading implementation
for subdomain in subdomains:
    t1 = threading.Thread(target=sub_domain, args=(subdomain,))
    t1.start()
    thread.append(t1)
```

---

## 💡 Pentesting Context

These scripts cover the **Reconnaissance phase** of 
a penetration test — the very first step in any 
real world engagement:

- **DNS Enumeration** reveals server infrastructure,
mail servers and hidden services
- **Subdomain Enumeration** uncovers hidden or 
forgotten subdomains that may have vulnerabilities

---

## 🔧 Built With

- Python 3
- `dnspython` — DNS queries
- `requests` — HTTP requests
- `threading` — Concurrent subdomain scanning
- `tqdm` — Progress bar
- `socket` — Connectivity checking

---

## 👨‍💻 Author

**Yousaf Rahil** — Aspiring Junior Pentester
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/yousaf-rahil-589a812a8)
