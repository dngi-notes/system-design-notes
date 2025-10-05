# Health Checks & Failover
## Table of Contents
- [Health Checks \& Failover](#health-checks--failover)
  - [Table of Contents](#table-of-contents)
  - [Purpose](#purpose)
  - [How it Works](#how-it-works)
    - [Health Checks](#health-checks)
      - [Active Health Checks](#active-health-checks)
      - [Passive Health Checks](#passive-health-checks)
    - [Failover Strategies](#failover-strategies)
  - [Tradeoffs](#tradeoffs)
    - [Pros](#pros)
    - [Cons](#cons)
  - [Real-World Examples](#real-world-examples)

## Purpose
Load Balancers must ensure they only send traffic to healthy servers. Health checks and failover mechanisms help maintain high availability by detecting and rerouting traffic when a server fails

Without them, users could be routed to **dead** or **slow** servers, causing downtime or poor performance.

## How it Works
### Health Checks
Health checks are a mechanism for verifying that backend services are functioning properly.

There are two types:
#### Active Health Checks
- The load balancer periodically pings/sends test requests (like an HTTP GET `/health` to each server)
- If a server fails several checks, it is marked as unhealthy and removed from the rotation
#### Passive Health Checks
- The load balancer monitors real traffic
- If it detects repeated timeouts or 5xx errors, it marks the server as unhealthy automatically

**Example**:
- NGINX might poll `/health` endpoint of each app server every 10 seconds
- If one fials to respond 3 times in a row, it is taken out of rotation until it recovers.

### Failover Strategies

| Strategy               | Description                                                                           | Example Use Case                                        |
| ---------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| **Automatic Failover** | LB automatically stops sending traffic to failed server and reroutes to healthy ones. | Blog server crashes → traffic goes to backup instantly. |
| **Manual Failover**    | Admin manually removes/restarts unhealthy node.                                       | Useful in maintenance windows.                          |
| **Hot Standby**        | Dedicated backup server already running and ready to take over.                       | Mission-critical systems needing near-zero downtime.    |
| **Cold Standby**       | Backup server started only after failure detected.                                    | Cost-efficient but slower recovery.                     |

## Tradeoffs
### Pros
- Prevents downtime by quickly removing bad servers
- Improves reliability and user experience
- Enables rolling updates with zero downtime

### Cons
- Frequent health checks consume resources
- Misconfiguration (if we're too aggressive/lenient) we may cause flapping &mdash; servers bouncing in/out of rotation
- Failover lag if detection time is too long

## Real-World Examples
- AWS ELB &ndash; automatically health-checks instances and reroutes traffic
- Kubernetes &ndash; uses liveness & readiness probes to decide if pods should receive traffic.
- NGINX/HAProxy &ndash; customizable health check intervals and thresholds