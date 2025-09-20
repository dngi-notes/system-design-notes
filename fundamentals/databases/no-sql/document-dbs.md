# Document Databases
## Table of Contents
- [Document Databases](#document-databases)
  - [Table of Contents](#table-of-contents)
  - [Purpose](#purpose)
  - [How it Works](#how-it-works)
    - [Example Query (find by username):](#example-query-find-by-username)
    - [Example Query (all posts by user):](#example-query-all-posts-by-user)
  - [Trade-offs](#trade-offs)
    - [Pros](#pros)
    - [Cons](#cons)
  - [Real World Examples](#real-world-examples)
  - [Schema Examples](#schema-examples)
    - [Option 1: Separate Collections (Relational Style)](#option-1-separate-collections-relational-style)
    - [Option 2: Embedded Documents (Document Style)](#option-2-embedded-documents-document-style)

## Purpose
Document DBs store data as documents (in a JSON-like format) instead of storing data in tables of rows.\
With document DBs we get:
- Flexible schemas (no strict columns)
- Good for apps where data shape changes over time
- Natural fit for modern APIs that use JSON already

## How it Works
- **Data Model**: Collections (like tables) contain documents (like rows)
- **Document**: JSON-like structure with nested fields
- **Schema**: Flexible &mdash; not all documents need the same fields
- **Queries**: Expressed in JSON-like syntax
### Example Query (find by username):
```js
db.users.find({ username: "alice"})
```

### Example Query (all posts by user):
```js
db.users.find({ user_id: ObjectId("12345") })
```
## Trade-offs
### Pros
- Flexible schemas
- Natural JSON format &rightarrow; good for web/mobile
- Embedding related data can avoid the need for joins

### Cons
- No strict schema (risks inconsistency)
- Complex relationships are harder to model than in relational DBs
- Queries across deeply nested structures can be slower

## Real World Examples
- Blogging platforms: Store posts with embedded comments
- E-commerce: Store product catalogs with variable attributes
- Mobile apps: JSON-based APIs &rightarrow; direct fit with MongoDB

*Interview Q: Design a document DB schema for a blogging platform*

## Schema Examples
### Option 1: Separate Collections (Relational Style)
```js
// Users
{
  _id: ObjectId("u1"),
  username: "alice",
  email: "alice@example.com",
  created_at: ISODate("2025-09-12")
}

// Posts
{
  _id: ObjectId("p1"),
  user_id: ObjectId("u1"),
  title: "My First Post",
  content: "Hello world!",
  created_at: ISODate("2025-09-12")
}

// Comments
{
  _id: ObjectId("c1"),
  post_id: ObjectId("p1"),
  user_id: ObjectId("u2"),
  content: "Nice post!",
  created_at: ISODate("2025-09-12")
}

```

### Option 2: Embedded Documents (Document Style)
```js
// Posts with embedded comments
{
  _id: ObjectId("p1"),
  user: {
    _id: ObjectId("u1"),
    username: "alice"
  },
  title: "My First Post",
  content: "Hello world!",
  created_at: ISODate("2025-09-12"),
  comments: [
    {
      _id: ObjectId("c1"),
      user: { _id: ObjectId("u2"), username: "bob" },
      content: "Nice post!",
      created_at: ISODate("2025-09-12")
    }
  ]
}
```