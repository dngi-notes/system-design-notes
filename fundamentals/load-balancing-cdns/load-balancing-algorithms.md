# Load Balancing Algorithms
## Table of Contents

- [Load Balancing Algorithms](#load-balancing-algorithms)
  - [Table of Contents](#table-of-contents)
  - [Purpose](#purpose)
  - [Common Algorithms](#common-algorithms)
    - [Round Robin](#round-robin)
    - [Least Connections](#least-connections)
    - [IP Hash](#ip-hash)
  - [Comparison Table](#comparison-table)
  - [Real World Examples](#real-world-examples)

## Purpose
Load balancing algorithms define how traffic is distributed across servers
- Goal: maximise performance, avoid overloads, and ensure fairness
- Different algorithms fit different traffic patterns

## Common Algorithms
### Round Robin
- Requests go to servers in a circular order: S1 &rightarrow; S2 &rightarrow; S3 &rightarrow; repeat
- Simple, with no need to track connection state

### Least Connections
- Directs traffic to the server with the fewest active connections
- Adapts dynamically if some requests are heavier

### IP Hash
- Hash of client's IP determines which server handles their requests
- Ensures a client is consistently routed to the same server (session stickiness)

## Comparison Table
| Algorithm         | Pros                                         | Cons                                         | When to Use                                                            |
|-------------------|----------------------------------------------|----------------------------------------------|-----------------------------------------------------------------------|
| Round Robin       | Simple, fair distribution, easy to implement | Doesn’t account for varying server load      | Uniform requests of similar size; basic traffic                       |
| Least Connections | Adapts to uneven load, balances heavy traffic| Slightly more overhead (tracks connections)  | When requests vary in duration/complexity                              |
| IP Hash           | Provides session stickiness, predictable routing| Uneven distribution if many clients share same IP| When user sessions need to persist on same server (e.g., shopping carts, logins) |

## Real World Examples
- **Round Robin** &rightarrow; CDN edge servers distributing static assets
- **Least Connections &rightarrow; API servers with long-lived requests
- **IP Hash** &rightarrow; Gaming servers or chat apps requiring session stickiness