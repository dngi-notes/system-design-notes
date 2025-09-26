# Cap Theorem
## Table of Contents
- [Cap Theorem](#cap-theorem)
  - [Table of Contents](#table-of-contents)
  - [Purpose](#purpose)
  - [How it Works](#how-it-works)
  - [Trade-offs](#trade-offs)
    - [Pros](#pros)
    - [Cons](#cons)
  - [Real-World Examples](#real-world-examples)
## Purpose
The **CAP theorem** (a.k.a Brewer's Theorem) states that in a **distributed database**, you can only **fully** guarantee two out of three properties:
- **Consistency (C)**: All nodes see the same data at the same time 
- **Availability (A)**: Every request gets a response, even if some nodes are down
- **Partition Tolerance (P)**: System continues to function even if network failures split it into parts

_**NOTE**: In real distributed systems, partition tolerance is **non-negotiable** (because networks can fail), so the choice is left between consistency and availability._

## How it Works
- Consistency (C):
  - Reads always return the most up-to-date write
  - _Example: Bank account transfer &rightarrow; both balances always match_
- Availability (A):
  - System responds &mdash; although data may be stale
  - _Example: Shopping sites always load product pages, even if the inventory updates are delayed_
- Partition Tolerance (P):
  - Network can break into disconnected segments, but system keeps working
  - _Example: Users in Europe and US still access their local replica, even if the cross-Atlantic link fails_

## Trade-offs
### Pros
- Helps architects choose DBs based on needs (strict consistency vs high availability)
### Cons
- Can't have all three at once
- Forces tough tradeoffs in real-world applications

## Real-World Examples
- **SQL Databases (CA)**
  - Prioritise Consistency + Availability
  - Example: Postgres, MySQL (single-node setups)
  - Downside: Not partition tolerant &rightarrow; if network breaks, DB becomes unavailable
- **Cassandra (AP)**
  - Prioritises Availability + Partition Tolerance
  - Example: Always returns responses even if some replicas are stale
  - Downside: Eventual consistency; stale reads possible
- **MongoDB (CP)
  - Prioritizes Consistency + Partition tolerance
  - Example: If leader goes down, the system blocks until a new primary is elected
  - Downside: Sacrifices availability during failover
*Interview Case: "In a distributed system, would you prefer stale but available data, or strongly consistent but sometimes unavailable data?"*
