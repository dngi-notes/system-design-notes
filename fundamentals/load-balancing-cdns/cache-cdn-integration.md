# Cache + CDN Integration
## Table of Contents
- [Cache + CDN Integration](#cache--cdn-integration)
  - [Table of Contents](#table-of-contents)
  - [Purpose](#purpose)
  - [How It Works](#how-it-works)
    - [Multi-Layer Caching Path](#multi-layer-caching-path)
    - [Cache Expiration and Invalidation](#cache-expiration-and-invalidation)
      - [Expiration (TTL):](#expiration-ttl)
      - [Cache Busting](#cache-busting)
    - [Coordination Example](#coordination-example)
  - [Trade-offs](#trade-offs)
    - [Pros](#pros)
    - [Cons](#cons)
    - [Real-World Examples](#real-world-examples)

## Purpose
Combining CDNs with **application level caching** creates a layered caching strategy that:
- minimizes latency at every step of data delivery (data is ready to go)
- reduces server and database load (since we dont need to request repeatedly)
- ensures that both static and dynamic content are delivered efficiently

> i.e. &rightarrow; CDN caches static assets (images, HTML, JS), Redis/Memcached store dynamic data (comments, posts)

## How It Works
### Multi-Layer Caching Path
1. Client Request &rightarrow; goes to CDN edge server
2. CDN Cache Check:
   1. if static file exists (cache hit), serve it immediately
   2. if it doesnt exists, retrieve it from the server, then cache it
3. App Server Cache Check:
   1. Uses Redis/Memcached to quickly return frequently accessed data (e.g. top articles)
   2. If data isn't cached &rightarrow; query the DB &rightarrow; store result in Redis for next time
4. Response travels back &rightarrow; cached by CDN &rightarrow; delivered to user

### Cache Expiration and Invalidation
#### Expiration (TTL):
- Redis entries might expire in minutes
- CDN static assets might expire in hours or days
#### Cache Busting
- Append version tags to file names (e.g. `main.v2.js`) or query params (`?v=2`)
- Ensures clients fetch new content after updates
- 
### Coordination Example
- App cache TTL: 5-10 minutes for "hot posts"
- CDN cache TTL: for 1-6 hours for static files
- On a new blog post publish &rightarrow; purge CDN cache + invalidate Redis entries

## Trade-offs
### Pros
- Extremely fast content delivery
- Reduces DB and origin server load
- Multi-layer resilience (if DB down, cached content still serves)

### Cons
- Cache invalidation complexity increases
- Must keep cache and CDN in sync
- Cache staleness ris if TTLs are not tuned properly

### Real-World Examples
- YouTube / Medium &rightarrow; CDNs for images/thumbnails, Redis for user feeds
- E-commerce sites &rightarrow; CDNs for product images, Redis for cart data
- Cloudflare + Redis stack &rightarrow; common setup in high-performance web apps

*Interview Case: How would you reduce response time for a page showing trending blog posts* 

&rightarrow; Cache hot posts in Redist (short TTL) and serve static assets via CDN (long TTL)