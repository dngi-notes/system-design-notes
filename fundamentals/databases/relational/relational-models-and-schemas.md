# Relational Models & Schemas

## Table of Contents
- [Relational Models \& Schemas](#relational-models--schemas)
  - [Table of Contents](#table-of-contents)
  - [Purpose](#purpose)
  - [How it Works](#how-it-works)
  - [Types of Relationships](#types-of-relationships)
  - [Trade-offs](#trade-offs)
  - [Real world examples](#real-world-examples)

## Purpose
The **relational model** organises data into structured tables that are easy to query, relate, and maintain.
It solves problems of unstructured storage by enforcing rules about how data is connected.

## How it Works
- **Tables** &rightarrow; Represents entities (e.g., `Users`, `Posts`, `Comments`)
- **Rows** &rightarrow; Individual records inside a table (e.g., one user, one post)
- **Columns** &rightarrow; Attributes of the entity (e.g. for a user: `username`, `first_name`, `email`)
- **Primary Key (PK)** &rightarrow; Unique identifier for each record (row) in the table (e.g. for a user: `user_id`)
- **Foreign Key (FK)** &rightarrow; Reference/Pointer to a primary key of another related table. Used to define relationships (e.g. `post_id` in `Comments` to link to `Posts`)

## Types of Relationships
- **One to One** &rightarrow; One user has a single profile
- **One to Many** &rightarrow; One user can write many posts
- **Many to Many** &rightarrow; (Optional Extension) Many users can like many posts

## Trade-offs
- *Pros*:
  - Ensures structure (no duplicate/invalid reference)
  - Easy to express relationships
  - Query language (SQL) powerful with joins and complex operations
- *Cons*
  - Complex schemas can get hard to maintain
  - Joins can be very costly at large scale
  - Overkill if relationships are minimal or data is unstructured

## Real world examples
- Blogging Platforms (Medium, WordPress)
- E-commerce (Users, Orders, Products, Reviews)
- Social Media (Users, Posts, Likes, Comments)
- **Potential Interview Problem** &rightarrow; Design a schema for an online forum