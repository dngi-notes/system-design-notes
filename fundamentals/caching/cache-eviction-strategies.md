# Cache Invalidation Strategies

## Table of Contents

- [Cache Invalidation Strategies](#cache-invalidation-strategies)
  - [Table of Contents](#table-of-contents)
  - [Purpose](#purpose)
  - [Common Strategies](#common-strategies)
    - [Write-Through](#write-through)
    - [Write-Around](#write-around)
    - [Write-Back (Write-Behind)](#write-back-write-behind)
    - [Eviction Policies (When Cache is Full)](#eviction-policies-when-cache-is-full)
  - [Strategies and Use Cases](#strategies-and-use-cases)
  - [Real World Examples](#real-world-examples)

## Purpose

Caching isn't only about storing &mdash; it's also about keeping data fresh while maintaining speed

- If the cache & DB diverge &rightarrow; a stale data problem arises
- Strategies define how writes interact with cache and DB
- Eviction policies handle when cache memory fills up

## Common Strategies

### Write-Through

- Write goes to cache + DB immediately
- Cache is always fresh, but slower rights

### Write-Around

- Write goes only to DB. Cache is updated on the next read (lazy)
- Reduces cache churn but first read may be stale/miss

### Write-Back (Write-Behind)

- Write goes to cache first, DB updated later (async)
- Fast writes, but risk of data loss if cache crashes before DB sync

### Eviction Policies (When Cache is Full)

- LRU (Least Recently Used): evict least recently accessed data
- LFU (Least Frequently Used): evict the items accessed the least frequently
- FIFO (First In, First Out): evict oldest entry regardless of use

## Strategies and Use Cases

| Strategy      | How it Works                                   | Pros                    | Cons                             | When to Use                                          |
|---------------|------------------------------------------------|-------------------------|----------------------------------|------------------------------------------------------|
| Write Through | Write to cache + DB at the same time           | Cache always consistent | Slower writes                    | When reads >> writes, consistency matters            |
| Write-Around  | Write only to DB, cache updated on next read   | Reduces cache churn     | First read may be stale/miss     | When writes are infrequent, cache churn is costly    |
| Write-Back    | Write to cache first, DB updated later (async) | Fast writes             | Risk of data loss if cache fails | When write speed is critical, can tolerate some risk |

## Real World Examples
- Write Through: User Profile updates
- Write Around: Product Catalog (Read more often than updated)
- Write Through: Logging, analytics (eventual consistency is okay)

**Interview Case**: If you cache user sessions what strategy would you use
*Answer: likely write-through to keep sessions consistent with the database*