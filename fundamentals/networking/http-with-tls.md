# Application of TLS in HTTP

- [Application of TLS in HTTP](#application-of-tls-in-http)
  - [Basics](#basics)
  - [Why TLS matters in System Design](#why-tls-matters-in-system-design)
  - [HTTPS Request Lifecycle](#https-request-lifecycle)
  - [System Design Considerations](#system-design-considerations)
    - [Performance](#performance)
    - [Scalability](#scalability)
    - [Security Design](#security-design)
    - [Placement of TLS in Architecture](#placement-of-tls-in-architecture)
  - [TLS Tradeoffs in System Design](#tls-tradeoffs-in-system-design)
  - [Real-World Practices](#real-world-practices)
  - [Key Takeaway](#key-takeaway)

## Basics
- HTTP (Hypertext Transfter Protocol): Application layer protocol for communication on the web
- TLS (Transfer Layer Security): Cryptographic protocol that provides confidentiality, integrity and authentication for data in transit
- HTTPS = HTTP + TLS &rightarrow; Secures HTTP traffic over TCP using TLS

## Why TLS matters in System Design
- Confidentiality: Encrypts requests/responses (e.g. login details, session cookies)
- Integrity: Prevents data tampering during transit
- Authentication Server (and optionally client) proves identity via digital certificates
- User Trust: HTTPS adoption improves UX and search ranking
- Compliance; Required for many standards (PCI-DSS, GDPR, HIPAA)

## HTTPS Request Lifecycle
1. TCP handshake (establishes connection)
2. TLS handshake:
   1. ClientHello &rightarrow; supported TLS versions, ciphers
   2. ServerHello &rightarrow; selects a cipher, sends certificate
   3. Key exchange &rightarrow; derive session keys
   4. Optional client authentication
3. Secure Data Transfer &rightarrow; All HTTP messages are now encrypted

## System Design Considerations
### Performance
- TLS handshake adds extra overhead (extra RTT)
- Mitigation strategies:
  - TLS session resumption (session IDs / session tickets)
  - HTTP/2 or HTTP/3 (multiplexing + reduced overhead)
  - TLS 1.3 (faster handshakes, 0-RTT)
  - Hardware Acceleration (SSL offloading on load balancers)

### Scalability
- Certificates need to be distributed across multiple servers
- Centralized certificate management (e.g. Let's Encrypt + ACME).
- Termination at load balancers / reverse proxies

### Security Design
- Forward secrecy &rightarrow; Ephemeral Diffie-Hellman
- Certificate pinning &rightarrow; Reduce MITM (man-in-the-middle) risk
- Strong cipher suites &rightarrow; Automatic certificate renewal (prevent outages)
- Protect private keys in HSMs or secure vaults

### Placement of TLS in Architecture
- **TLS Termination at Edge** (common)
  - TLS is terminated at a load balancer, proxy, or CDN
  - Internal traffic may be plain HTTP (tradeoff: performance vs internal security)
- **End-to-End TLS**
  - TLS all the way from client to backend services
  - Higher security but more computational cost
- **mTLS (Mutual TLS)**
  - Used in microservices & zero-trust architectures
  - Both client and server present certificates

## TLS Tradeoffs in System Design
- **Performance vs Security**: Terminate TLS at edge for performance; but sensitive environments (finance, healthcare) often use end-to-end TLS
- **Complexity vs Usability**: mTLS adds strong authentication but complicates certificate management
- **Cost vs Scale**: TLS offloading appliances/CDNs reduce server CPU load but increase infrastructure costs

## Real-World Practices
- **Web applications**: TLS termination at load-balancer + internal HTTP
- **APIs**: HTTPS + OAuth/JWT, often with mTLS for B2B integrations
- **Microservices**: Service mesh (e.g. Istio, Linkerd) manages TLS between services transparently
- **Mobile/IoT**: TLS with certificate pinning to prevent fake CA attacks

## Key Takeaway
> In system design, TLS transforms HTTP into HTTPS, ensuring secure communication. Where and how TLS is applied (termination, end-to-end, or mutual authentication) depends on security requirements, performance goals, and system complexity.