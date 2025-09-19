# Databases vs Flat Files

## Table of Contents
- [Databases vs Flat Files](#databases-vs-flat-files)
  - [Table of Contents](#table-of-contents)
  - [Purpose](#purpose)
  - [How it Works](#how-it-works)
    - [Flat Files](#flat-files)
    - [Databases](#databases)
  - [Key Concepts Explained](#key-concepts-explained)
  - [Tradeoffs](#tradeoffs)
    - [Flat Files](#flat-files-1)
      - [Pros](#pros)
      - [Cons](#cons)
    - [Databases](#databases-1)
      - [Pros](#pros-1)
      - [Cons](#cons-1)
  - [Real-World Examples](#real-world-examples)
    - [Flat files](#flat-files-2)
    - [Databases](#databases-2)
  - [Supporting Images/Diagrams](#supporting-imagesdiagrams)

## Purpose
Databases exist to manage data more efficiently than flat files.
They solve problems like:
- **Persistence**: Keeping data safe across crashes/power loss
- **Concurrency**: Ensuring multiple users/programs can safely read & write at the same time
- **Querying** Efficiently finding, filtering and manipulating data without manually scanning everything

Without a database, data access becomes slow unsafe, and hard to manage as systems grow.

## How it Works
### Flat Files
- Store text in plain text/CSV/JSON
- Good for small amounts of data, but there are no mechanisms for safety or fast retrieval

### Databases
- Uses structured storage + query engine (e.g. SQL)
- Provides guarantees and optimizations

## Key Concepts Explained
- ### Persistence
  - In databases &rightarrow; Data is written to disk with logs/checkpoints to survive crashes
  - In flat files, we risk corruption if a write is interrupted
- ### Concurrency
  - In databases &rightarrow; Transactions + locking mechanisms ensure the data remains consistent (e.g., two people cant withdraw the same €100 simultaneously)
  - In flat files &rightarrow; Simultaneous access can overwrite or corrupt data
- ### Querying
  - In databases &rightarrow; You can use SQL/other querying languages to search/filter/join large datasets quickly using indexes
  - In flat files &rightarrow; You would have to manually scan each line or load everything into memory

## Tradeoffs
### Flat Files
#### Pros
- Simple to set up
- Good for small single user apps
- Human readable (CSV, JSON)

#### Cons
- No structured enforcement (easy to insert bad data)
- Doesnt handle concurrency
- Easy corruption if multiple writes happen at once
- Searching large files is slow

### Databases
#### Pros
- Reliable persistence and consistency
- Safe for users (ACID)
- Powerful, efficient querying
- Tools for scaling + analytics

#### Cons
- More time needed for setup
- Requires learning query languages
- Overkill for small projects

## Real-World Examples
### Flat files
- Game config files
- Spreadsheets
- Logs

### Databases
- Bank transaction systems
- Ecommerce inventories
- Social media posts
- Hospital records

**Example Interview Question**: *How would you design a ticket booking system? Why is a DB necessary over flat files*


## Supporting Images/Diagrams
...