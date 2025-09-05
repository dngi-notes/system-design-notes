# DNS

## Table of Contents
- [DNS](#dns)
  - [Table of Contents](#table-of-contents)
  - [📌 DNS Basics](#-dns-basics)
  - [📌 DNS Records (must know)](#-dns-records-must-know)
  - [📌 DNS Resolution Flow](#-dns-resolution-flow)
  - [📌 DNS Caching \& TTL](#-dns-caching--ttl)
  - [📌 Reverse DNS (PTR Records)](#-reverse-dns-ptr-records)
  - [📌 DNS in System Design](#-dns-in-system-design)
  - [📌 DNS Security](#-dns-security)
  - [📌 Common Issues \& Pitfalls](#-common-issues--pitfalls)

## 📌 DNS Basics
- **Meaning**: Domain Name System
- **Purpose**: Maps human-readable names/addresses e.g. (example.com) to IP addresses
- **Hierarchy**: Root &rightarrow; Top Level Domain (TLD) e.g. (.com, .org, .net) &rightarrow; Authoritative DNS &rightarrow; Records.
- **Distributed & Hierarchial**: No single server stores all records

## 📌 DNS Records (must know)
- **A record**: Domain &rightarrow; IPv4 address
- **AAAA record**: Domain &rightarrow; IPv6 address
- **CNAME**: Alias &rightarrow; Canonical Domain (good for load balancing/CDNs)
- **MX**: Mail servers for a domain
- **TXT**: Arbitrary text (SPF, DKIM, verification)
- **NS**: Points to authoritative name servers
- **SRV**: Service discovery (protocol + port)

## 📌 DNS Resolution Flow
  1. Client &rightarrow; Recursive Resolver (usually ISP, or public like `8.8.8.8`)
  2. Resolver checks **cache**
  3. If not cached &rightarrow; query the root &rightarrow; TLD &rightarrow; Authoritative server
  4. Response cached by resolver + client

## 📌 DNS Caching & TTL
- **TTL (Time To Live)**: how long a record can be cached by resolvers/browsers
- **Where caching happens**:
  - browser cache
  - OS cache
  - recursive resolver cache (e.g. `8.8.8.8`)
- **Tradeoff**:
  - Short TTL &rightarrow; faster updates, but more queries
  - Long TTL &rightarrow; less load, but more updates

## 📌 Reverse DNS (PTR Records)
- **PTR record**: Maps IP &rightarrow; **Domain name** (opposite of A/AAAA records)
- Used for logging, email spam prevention, and verification
- Example: `8.8.8.8 -> dns.google`.

## 📌 DNS in System Design
- **Load Balancing**: Multiple A/AAAA records &rightarrow; simple round robin
- **GeoDNS / Anycast**: Serve nearest server  based on client location/network
- **CDNs**: CNAMEs often used to route requests to CDN providers
- **Failover**: Health checks + short TTLs to quickly switch to backup servers
- **Service Discovery**: SRV/TXT records used by microservices

## 📌 DNS Security
- **DNSSEC (Domain Name System Security Extensions)**:
  - Uses cryptographic signatures to verify authenticity of DNS records
  - Prevents cache poisioning / man-in-the-middle-attacks
- **Common attacks**:
  - **DNS Spoofing / Cache Poisoning**: fake responses inserted in cache
  - **DDos amplification** using open resolvers to flood targets
  - **Tunneling**: exfiltration of data via queries

## 📌 Common Issues & Pitfalls
- **Propagation Delay**: DNS changes can take hours to update worldwide
- **Stale Cache**:  Clients may keep old DNS entries
- **Split-horizon DNS**: Different results for internal vs external queries
- **Single point of failure** If authoritative servers go down, the entire domain is unavailable
- **Misconfigured MX/TXT** records. Can break email delivery or cause spam flagging

