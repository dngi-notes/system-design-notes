# Replication
## Table of Contents
- [Replication](#replication)
  - [Table of Contents](#table-of-contents)
  - [Purpose](#purpose)
    - [Replication Models](#replication-models)
    - [Sync vs Async](#sync-vs-async)
  - [Trade-offs](#trade-offs)
    - [Pros](#pros)
    - [Cons](#cons)
  - [Real World Examples](#real-world-examples)

## Purpose
### Replication Models
- **Master-Slave (Leader/Follower)**:
  - One master/leader handles **writes**
  - Slaves/followers replicate the data and handle reds
  - Good for scaling reads, but writes are bottlenecked at the master

- **Master-Master (Multi-leader)**:
  - Multiple masters can accept writes
  - Each master replicates changes to others
  - Good for scaling but introduces conflict resolution challenges

### Sync vs Async
- **Synchronous Replication**
  - Write is only "committed" when replicas confirm
  - Guarantees consistency, but slower
- **Asynchronous Replication**
  - Master/Leader commits immediately, replicas update later
  - Faster, but risk of data loss if master fails before replicas sync

## Trade-offs
### Pros
- Improves fault tolerance & uptime
- Enables load balancing for reads
- Critical for global, large scale systems

### Cons
- Sync &rightarrow; latency overhead
- Async &rightarrow; possible stale reads or data loss on failure
- Master-master &rightarrow; conflict handling needed

## Real World Examples
- MySQL Replication &rightarrow; common in web apps (master for writes, replicas for reads)
- MongoDB Replica Sets &rightarrow; built in replication with automatic failover
- Cassandra &rightarrow; uses peer to peer replication across nodes
*Interview Case: "If your primary DB goes down, how do replicas keep the system available?"*