# Memcached Basics
## Table of Contents
- [Memcached Basics](#memcached-basics)
  - [Table of Contents](#table-of-contents)
  - [Purpose](#purpose)
  - [How it works](#how-it-works)
  - [Trade-offs (Redis vs Memcached)](#trade-offs-redis-vs-memcached)
  - [Real-World Examples](#real-world-examples)

## Purpose
Memcached is a high-performance, distributed, in-memory cache used to speed up dynamic web-apps by reducing database load
- Stores key-value pairs in memory
- Designed to be simple and lightweight
- Focus: **pure caching** (no persistence, no advanced data structures)

## How it works
- `All data is stored as `{key : value}` pairs in RAM
- Supports strings and objects (after serialization)
- Has TTL (expiration time) for entries
- If memory is full, old data is evicted using LRU (least recently used)

## Trade-offs (Redis vs Memcached)

| Feature     | Redis                                     | Memcached                                           |
|-------------|-------------------------------------------|-----------------------------------------------------|
| Data Types  | Strings, lists, hashes, sets, sorted sets | Strings only (simple key-value)                     |
| Persistence | Yes (RDB, AOF, snapshots)                 | No (pure in-memory, data lost on restart)           |
| Scaling     | Cluster mode, replication, sharding       | Simple distributed sharding                         |
| Performance | Slightly heavier but versatile            | Extremely lightweight, raw speed for simple lookups |
| Use Cases   | Caching, queues, leaderboards, sessions   | Pure caching layer for DB queries/pages             |
| When to Use | When you need rich features + persistence | When you need the fastest, simplest cache           |

## Real-World Examples
- **Memcached**: 
  - Facebook originally used Memcached heavily for scaling feed reads
  - Ecommerce to cache product catalog pages
- **Redis**
  - More common today because of its versatility (used for caching, sessions, leaderboards, queues)
*Interview Case: When would you use Memcached over Redis?*
**Answer: If you need simnple fast cache with no persistence or fancy structures**