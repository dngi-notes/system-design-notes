# Caching
## Table of Contents
- [Caching](#caching)
  - [Table of Contents](#table-of-contents)
  - [Purpose](#purpose)
  - [How it Works](#how-it-works)
    - [TTL (Time To Live)](#ttl-time-to-live)
  - [Trade-offs](#trade-offs)
    - [Pros](#pros)
    - [Cons](#cons)
  - [Real-World Examples](#real-world-examples)

## Purpose
Caching stores frequently **accessed/expensive-to-compute** data in a faster, temporary storage layer
- It reduces **database load** (_fewer queries_)
- It improves **response times** (_faster user experience_)
- It helps handle traffic spikes (_scales better_)

## How it Works
- **Client-side Cache** &rightarrow; Browser caches static files (CSS, JS, images)
- **CDN (Content Delivery Network)** &rightarrow; Stores content closer to users geographically
- **Server-side Cache** &rightarrow; App caches rendered pages, computed results, or API responses
- **Database Query Cache** &rightarrow; Stores results of frequent queries (e.g. "Top 10 Posts")

### TTL (Time To Live)
- Cached data can expire after $X$ seconds/minutes
- Prevents stale content from living forever

## Trade-offs
### Pros
- Faster responses.
- Reduces database and backend load.
- Handles traffic spikes better
### Cons
- Risk of **stale data** (cache not updated in time)
- Complexity in deciding what & when to cache
- Cache invalidation (keeping cache consistent with DB) is hard

## Real-World Examples
**Medium** &rightarrow; cache hot posts at multiple layers (CDN + server-side)
**E-commerce** &rightarrow; cache product catalog pages for speed
**Gaming Leaderboards** cached in redis for fast lookups
*Interview Case: "What caching strategy would you use for a blog homepage showing top posts and why?*