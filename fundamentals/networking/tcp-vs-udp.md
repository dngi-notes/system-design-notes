# TCP VS UDP

## Table of Contents
- [TCP VS UDP](#tcp-vs-udp)
  - [Table of Contents](#table-of-contents)
  - [Core Differences](#core-differences)
    - [TCP](#tcp)
      - [**Transmission Control Protocol (TCP)**](#transmission-control-protocol-tcp)
    - [UDP](#udp)
      - [**User Datagram Protocol (UDP)**](#user-datagram-protocol-udp)
  - [Key Notes for System Design](#key-notes-for-system-design)
  - [Interview Level Insights](#interview-level-insights)

## Core Differences
### TCP
#### **Transmission Control Protocol (TCP)**
  - **Connection Oriented**: Requires a handshake before communication
  - **Reliable**: Guarantees packet delivery, order, and error checking
  - **Flow control & congestion control**: Prevents overwhelming receivers and networks
  - **Heavier overhead**: More metadata and state tracking
  - **Use cases**: Web browsing (HTTP/HTTPS), file transfer(FTP), email (SMTP/IMAP), remote access (SSH)
  
### UDP
#### **User Datagram Protocol (UDP)**
- **Connectionless**: Just sends packets, no handshake
- **Unreliable**: No guarantee of delivery, order, or duplicates
- **Lightweight**: Very little overhead
- **Faster**: Lower latency due to minimal checks
- **Use cases**: Realtime apps (VoIP, video streaming, gaming), DNS lookups, DHCP

## Key Notes for System Design
1. **Handshake vs No Handshake**
   - TCP requires a 3 way handshake (SYN &rightarrow; SYNC-ACK &rightarrow; ACK) before sending data 
   - UDP skips this, making it suitable for low-latency needs.
2. **Reliability Tradeoffs**
   - TCP provides reliability at the cost of latency and throughput
   - UDP gives speed but forces reliability to be handled in the application layer
3. **Ordering**
   - TCP ensures ordered delivery (packets assembled in sequence)
   - UDP packets may arrive out of order, be duplicated, or lost
4. **Performance Considerations**
   - TCP can cause "head-of-line blocking" &rightarrow; if one packet is lost, the others wait
   - UDP avoids this but requires custom handling for ordering and retries
5. **Security**
    - Both can be encrypted (TCP &rightarrow; Transport Layer Security (TLS); UDP &rightarrow; Datagram Transport Layer Security (DTLS)/ Quick UDP Internet Connections (QUIC))
    - QUIC (used in HTTP/3) is important &mdash; built on UDP for speed, with reliability and encryption added.
6. **When to choose TCP vs UDP in design**
    - **TCP**: if correctness, ordering, and completeness matter more than latency (e.g. financial transactions, APIs)
    - **UDP**: if low latency matters more than perfect delivery (e.g. video streaming, gaming, video chat)

## Interview Level Insights
- Many modern protocols use UDP + reliability at higher levels (e.g., QUIC/HTTP3) for speed
- Thing of user experience trade-offs:
  - Video buffering &rightarrow; TCP okay
  - Live call &rightarrow; UDP better even with dropped packets
- In distributed systems sometimes UDP is chosen for service discovery because it is lightweight