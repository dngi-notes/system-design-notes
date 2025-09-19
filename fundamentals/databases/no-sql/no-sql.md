# NoSQL
## Table of Contents
- [NoSQL](#nosql)
  - [Table of Contents](#table-of-contents)
  - [Purpose](#purpose)
  - [How it Works](#how-it-works)
    - [1. Key-Value Stores](#1-key-value-stores)
    - [2. Document Stores](#2-document-stores)
    - [3. Columnar (Wide-Column) Stores](#3-columnar-wide-column-stores)
    - [4. Graph Databases](#4-graph-databases)
    - [Comparison](#comparison)
  - [Real-World Examples](#real-world-examples)

## Purpose
NoSQl databases were designed to handle **large-scale, distributed, flexible data** where relational databases can struggle.
- Schema Flexibility
- Horizontal Scaling (across many servers)
- Optimized for specific data access patterns

## How it Works
### 1. Key-Value Stores
- Simplest: store data as `{key : value}`
- Example: Redis, DynamoDB
- Great for cachinng, sessions, fast lookups

### 2. Document Stores
- Store semi-structured data as documents (JSON-like)
- Example: MongoDB, CouchDB
- Flexible schema, good for evolving apps

### 3. Columnar (Wide-Column) Stores
- Store data by columns instead of rows
- Example: Cassandra, HBase
- Optimised for analytics & big data queries

### 4. Graph Databases
- Store entities + relationships as nodes & edges
- Example: Neo4j
- Ideal for highly connected data (social networks, recommendations)

### Comparison
| Type | Advantages | Disadvantages | Best Use Cases |
|------|------------|---------------|----------------|
| **Key-Value** | Very fast, simple, scalable | No query flexibility, value opaque | Caching, sessions, quick lookups |
| **Document** | Flexible schema, rich queries, natural JSON | Harder joins, can bloat with deep nesting | Content management, evolving app schemas |
| **Columnar** | Scales horizontally, good for analytics | Complex to model, eventual consistency | Time-series data, big data analytics |
| **Graph** | Excellent for relationships, graph queries | Slower for large flat datasets | Social networks, fraud detection, recommendations |

## Real-World Examples
- **Key-Value**: Redis for caching, DynamoDB for shopping carts
- **Document**: MongoDB powering flexible APIs
- **Columnar**: Cassandra for Netflix's viewing history
- **Graph**: Neo4j for LinkedIn connections

**Interview Case:** "*Which NoSQL DB type would you pick for `<use case>`*"