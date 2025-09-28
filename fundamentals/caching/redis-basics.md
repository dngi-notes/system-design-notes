# Redis Basics
## Table of Contents
- [Redis Basics](#redis-basics)
  - [Table of Contents](#table-of-contents)
  - [Purpose](#purpose)
  - [How it Works](#how-it-works)
    - [Data Types](#data-types)
    - [TTL (Time-To-Live)](#ttl-time-to-live)
  - [Trade-offs](#trade-offs)
    - [Pros](#pros)
    - [Cons](#cons)
  - [Real-World Examples](#real-world-examples)

## Purpose
Redis is an **in-memory key-value store** designed for speed and flexibility
- Stores frequently accessed data for ultra-fast lookups
- Great for caching, real-time analytics, leaderboards, and sessions

## How it Works
### Data Types
- **String** &rightarrow; simplest, like `"key" : "value"`
- **List** &rightarrow; an ordered collection, like a queue or stack
- **Hash** &rightarrow; key-value pairs inside on Redis key (like an object; embedded structure)
- **Set** &rightarrow; unique, unordered collection
- **Sorted Set** A set with scores (useful for leaderboards)

### TTL (Time-To-Live)
- Keys can expire after a set duration
- Prevents stale data from staying in the cache
- Example:
```bash
    SET hot_post "post_123"
    EXPIRE hot_post 3600  #expires after 1 hour (3600 seconds)
```

## Trade-offs
### Pros
- Fast
- Flexible data structures
- Simple commands for caching and sessions

### Cons
Memory limited (RAM is expensive)
Persistence options weaker than traditional DBs
Best for temporary cache use, not full primary storage

## Real-World Examples
- Blog caching: store popular articles
- Session management: user sessions
- Leaderboards: gaming
*Interview case: How would you store a shopping cart in Redis?*