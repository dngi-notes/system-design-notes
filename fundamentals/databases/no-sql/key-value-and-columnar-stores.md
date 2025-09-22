# Key Value Stores
- [Key Value Stores](#key-value-stores)
  - [Purpose](#purpose)
  - [How it Works](#how-it-works)
    - [Redis (Key-Value Store)](#redis-key-value-store)
    - [Cassandra (Columnar Store)](#cassandra-columnar-store)
  - [Trade-offs](#trade-offs)
  - [Real-world Examples](#real-world-examples)
    - [Redis:](#redis)
    - [Cassandra](#cassandra)


## Purpose
- **Key Value Stores (e.g. Redis)**: 
  - Optimise for ultra-fast lookups using a simple `{key : value}` model
  - Great for caching, sessions, or quick retrieval
- **Columnar Stores (e.g. Cassandra)**:
  - Store data by **columns instead of rows**, enabling efficient analytics, time-series and high-volume writes across distributed systems

## How it Works
### Redis (Key-Value Store)
- Data stored as pairs `key : value`
- Values can be strings, hashes, lists, sets, sorted sets
- Data is kept in memory for speed (optionally persisted)
- Common operations:
```bash
SET user:1:name "Alice"
GET user:1:name
```

### Cassandra (Columnar Store)
- Data grouped by column families (similar to tables, but more flexible)
- Optimized for distributed writes and reads
- *Example: Blog posts could be stored with post_id as the partition key, and comments as clustered columns*
- Query patterns are designed up-front → schema fits how data will be accessed.

## Trade-offs

| Type | Pros | Cons | When to Use |
|------|------|------|-------------|
| **Key-Value** | Ultra-fast, simple, scalable, in-memory | No query flexibility, only lookup by key | Caching, sessions, quick retrieval |
| **Columnar** | Great for analytics, time-series, massive writes | Complex modeling, eventual consistency trade-offs | Large-scale apps, logs, IoT, analytics |

## Real-world Examples
### Redis:
- Caching rendered blog pages
- Storing user sessions
- Leaderboards in gaming

### Cassandra
- Netflix viewing history
- Time-series metrics for monitoring
- IoT sensor data ingestion
**Interview Case**: *When would you use Redis vs Cassandra?*