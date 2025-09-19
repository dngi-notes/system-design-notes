# Indexes and Queries
## Table of Contents
- [Indexes and Queries](#indexes-and-queries)
  - [Table of Contents](#table-of-contents)
  - [Purpose](#purpose)
  - [How it Works](#how-it-works)
    - [Indexes (B-Tree Basics)](#indexes-b-tree-basics)
    - [SELECT Queries](#select-queries)
    - [JOINs](#joins)
  - [Trade-offs](#trade-offs)
    - [Pros of Indexes](#pros-of-indexes)
    - [Cons](#cons)
  - [Real-world Examples](#real-world-examples)

## Purpose
Indexes and Queries exist to make data retrieval **efficient and flexible**
- Without an index &rightarrow; The database has to scan the entire table (slow for large databases)
- With an index &rightarrow; The database can quickly find the required rows/records (like a book's index)
- Queries (via SQL) let us filter/combine/analyze data without manual scanning

## How it Works
### Indexes (B-Tree Basics)
- A database **index** is a data structure (commonly a B-tree) that maps keys to their row locations
- B-Trees are balanced trees &rightarrow; lookup/search operations are efficient ($O(log\space n)$)
- *Example: Searching for a `user_id = 123` in a table of 1M users is instant when using an index*
**Without an index**: Full table scan (check every row)
**With an index**: Jump directly to the row like in a phonebok

### SELECT Queries
- `SELECT` &rightarrow; SQL keyword to retrieve data
- Syntax:
```sql
SELECT column1, column2
FROM table
WHERE condition;
```
- Example:
```sql
SELECT username, email
from users
WHERE user_id = 123;
```

### JOINs
- `JOIN` &rightarrow; combines rows from two (or more) tables based on relationships
- Types:
  - **`INNER JOIN`** &rightarrow; Only matching rows in both tables
  - **`LEFT JOIN`** &rightarrow; All rows from the left and the matching rows from the right
  - **`RIGHT JOIN`** &rightarrow; All rows from the right and the matching rows from the left
  - **`FULL OUTER JOIN`** &rightarrow; All rows from both tables, matching where possible
- *Example: Get all posts with the author's username*
```sql
SELECT Posts.title, Users.user_name
FROM Posts
JOIN Users ON Posts.user_id = Users.user_id
```

## Trade-offs
### Pros of Indexes
- Huge speed improvement for read-heavy databases
- Enables efficient lookups, filtering and joins

### Cons
- Extra storage overhead
- Slows down writes (insert/update/delete must also update indexes)
- Choosing the wrong index may waste resources

## Real-world Examples
- **E-commerce:**: Index on `product_id` speeds up product lookups
- **Social Media**: Index on `user_id` or `post_id` to fetch feeds
- *Interview Case: ""Why does indexing help? Show difference between scanning 1M rows, vs jumping directly to the right one*