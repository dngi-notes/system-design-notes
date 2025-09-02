# IP Addresses & Routing

- [IP Addresses \& Routing](#ip-addresses--routing)
  - [Basics of IP Addresses](#basics-of-ip-addresses)
    - [What is an IP Address](#what-is-an-ip-address)
    - [Structure of IP Addresses](#structure-of-ip-addresses)
    - [Types of IP Addresses](#types-of-ip-addresses)
    - [CIDR (Classless Inter-Domain Routing)](#cidr-classless-inter-domain-routing)
  - [Basics of Routing](#basics-of-routing)
    - [Types of routing](#types-of-routing)
    - [Routing Concepts](#routing-concepts)
  - [NAT \& Load Balancing](#nat--load-balancing)
  - [IP Application in System Design](#ip-application-in-system-design)
    - [Common patterns](#common-patterns)
    - [Challenges](#challenges)
  - [Routing in Large Scale Systems](#routing-in-large-scale-systems)
  - [Best Practices for System Design](#best-practices-for-system-design)


## Basics of IP Addresses
### What is an IP Address
- An **IP Address** is a unique identifier for devices on a network
- split up into 2 types:
  - **IPv4**: 32-bit address (e.g. `192.168.1.1`) &rightarrow; ~4.3B addresses
  - **IPv6**: 128-bit address (e.g. `2001:db8::1`) &rightarrow; practically unlimited addresses

### Structure of IP Addresses
- **IPv4**: `A.B.C.D` (dotted decimial, each octet = 8 bits)
- **IPv4**: Hexadecimal, separated by `:` (e.g., `fe80::1`)

### Types of IP Addresses
- **Private IP**: For internal networks, not routable on the internet
  - IPv4 ranges:
    - `10.0.0.0/8`
    - `172.16.0.0/12`
    - `192.168.0.0/16`
- **Public IP**: Globablly unique, routable
- **Loopback**: Allows a computer to communicate with itself without using a physical network 
  - `127.0.0.1` (localhost)
- **Link-local**: Auto-assigned for local comms 
  - (`169.254.0.0/16` in IPv4)
- **Multicast/Broadcast**: One-to-many communication

### CIDR (Classless Inter-Domain Routing)
- Defines **subnets** using prefix length (`/24`, `/16`, etc)
  - Example 192.168.1.0/24 &rightarrow; 256 IPs (254 usable)
- Important for **scalability, segmentation, and efficient routing**

## Basics of Routing
Routing = deciding where packets go

### Types of routing
1. **Direct Routing**: Source and destination on the same subnet &rightarrow; no router needed
2. **Static Routing**: Admin-configured routes &rightarrow; simple, predictable, but not scalabale
3. **Dynamic Routing**: Routers exchange routes automatically.
   - **Interior Gateway Protocols (IGPs)**
     - RIP (obsolete, distance vector)
     - OSPF (link-state, hierarchial)
     - EIGRP (Cisco proprietary)
   - **Exterior Gateway Protocols (EGPs)**
     - BGP &rightarrow; the backbone of the internet

### Routing Concepts
- **Default Gateway**: Router to forward traffic outside local subnet.
- **Route Table**: Maps destination networks &rightarrow; next hop.
- **Longest Prefix Match**: Router chooses the most specific subnet route.

## NAT & Load Balancing
- **NAT (Network Address Translation):** Maps private IPs to public IPs.
  - **SNAT (Source NAT)**: &rightarrow; outbound traffic
  - **DNAT (Destination NAT):** &rightarrow; inbound traffic
  - **PAT (Port Address Translation:**) &rightarrow; multiple private IPs &rightarrow; one public IP (home routers).
- **Load Balancers**: Distribute traffic across multiple servers
  - L4 (IP + Port based)
  - L7 (Application-aware, e.g. HTTP headers).

## IP Application in System Design
- When designing distributed systems, networks are critical:
### Common patterns
- **Private Subnets** (e.g. DB servers not internet-exposed)
- **Public Subnets** (APIs, application frontend)
- **VPCs (Virtual Private Clouds)** in AWS/Azure/GCP
- **Peering and VPNs** for interconnecting private networks

### Challenges
- **Scaling** - subnet size planning (avoid running out of IPs)
- **Routing complexity**: multi-region, hybrid cloud setups
- **Latency** - routing path selection affects performance
- **Security** - firewalls, ACLs, segmentation
- **Multi-tenancy** - avoid overlapping private IP ranges

## Routing in Large Scale Systems
- **Anycast IPs**: same IP address being advertised from multiple locations &rightarrow; requests routed to nearest instance (used in CDNs, DNS)
- **Overlay Networks**: Software-defined routing over physical networks (e.g. Kubernetes CNI, service meshes)
- **Service Discovery**: Instead of static IPs, use DNS, load balancers or service meshses.

## Best Practices for System Design
- Use CIDR blocks carefully for scalability.
- Separate public-facing and private subnets.
- Use NAT gateways for outbound-only services.
- Apply firewalls/security groups with least privilege.
- Plan for multi-region/multi-cloud routing early.
- For global services, combine:
  - Anycast + DNS-based load balancing
  - BGP-aware routing
  - Local routing optimizations