# CDN Basics
## Table of Contents
- [CDN Basics](#cdn-basics)
  - [Table of Contents](#table-of-contents)
  - [Purpose](#purpose)
  - [How it Works](#how-it-works)
    - [Geographically Distributed Edge Servers](#geographically-distributed-edge-servers)
    - [Request flow](#request-flow)
    - [Key Concepts](#key-concepts)
  - [Tradeoffs](#tradeoffs)
    - [Pros](#pros)
    - [Cons](#cons)
  - [Real-World Examples](#real-world-examples)

## Purpose
A CDN (Content Delivery Network) distributes and caches static content (e.g. images, CSS, JS, videos, etc) on servers located closer to end users

This reduces latency, improves load times, and offloads the origin server, leading to better scalability and uptime.

In short:
> a CDN brings your content closer to your users, not your users closer to your severs

## How it Works
### Geographically Distributed Edge Servers
- CDNs have nodes ("edge servers") all over the world
- Each edge node caches content from your origin server

### Request flow
- When a user requests content (like an image):
  - The CDN checks if it has a cached copy
  - If yes &rightarrow; it serves it directly
  - If no &rightarrow; it fetches from the origin server, then caches it for next time

### Key Concepts
- Edge Location: Closest CDN server to the user
- Origin server: the main app or database server
- TTL (Time to Live) determines how long content stays cached
- Cache Invalidation: Mechanism to remove outdated contennt from CDN

## Tradeoffs
### Pros
- Reduces latency (faster page loads)
- Offloads bandwidth from origin server
- Improves availability and fault tolerance
- Protects against DDOS (some CDNs include security features)
### Cons
- Cost for high traffic/enterprise plans
- Cache invalidation can be tricky
- Dynamic content can't always be cached
- Adds setup/configuration complexity

## Real-World Examples
- Cloudflare: global CDN
- Akamai: one of the oldes and largest enterprise CDNs
- AWS CloudFront: integrates well with AWS S3