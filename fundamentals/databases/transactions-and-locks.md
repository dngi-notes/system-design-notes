# Transactions and Locks
## Table of Contents
- [Transactions and Locks](#transactions-and-locks)
  - [Table of Contents](#table-of-contents)
  - [Purpose](#purpose)
  - [How it Works](#how-it-works)
    - [Locks](#locks)
    - [Isolation Levels](#isolation-levels)
      - [1. Read Uncommitted (weakest)](#1-read-uncommitted-weakest)
      - [2. Read Committed](#2-read-committed)
      - [3. Repeatable Read](#3-repeatable-read)
      - [4. Serializable (strongest)](#4-serializable-strongest)
  - [Trade-offs](#trade-offs)
    - [Pros:](#pros)
    - [Cons:](#cons)
  - [Real World Examples](#real-world-examples)
      - [Deadlock case](#deadlock-case)
      - [Interview case](#interview-case)
  - [Diagram Idea](#diagram-idea)

## Purpose
When multiple transactions run at the same time (concurrency), databases use **locks** and **isolation levels** to keep data consistent
- **Locks**: Prevent two operations from conflicting (e.g. two users trying to update the same row)
- **Isolation Levels**: Define how much transactions can "see" each other's intermediate changes
- **Goal**: Balance consistency vs performance

## How it Works
### Locks
- A **lock** is a mechanism that prevents unsafe concurrent access
- **Example**: *If one transaction is updating `account_balance`, another must wait before reading/writing it*
- -**Deadlock**: When two transactions each hold a lock that the other needs &rightarrow; both wait forever (DB must detect and resolve)

### Isolation Levels
Isolation defines how visible uncommitted/ongoing changes are:
#### 1. Read Uncommitted (weakest)
- Transactions can read uncommitted data ("dirty reads)
- Example: *See a $100 transfter before it's commited &mdash; might dash if rolled back.
#### 2. Read Committed
- Can only read committed data
- Prevents dirty reads, but non-repeatable reads stil possible (data changing between two reads)
#### 3. Repeatable Read
- Guarantees same result for repeated reads within one transaction
- Prevents dirty & non-repeatbale reads, but phantom rows (new rows added by another transaction) may still appear
#### 4. Serializable (strongest)
- Transactions behave as if executed one after another (full isolation).
- Prevents dirty reads, non-repeatable, and phantoms
- Safest but most expensive (lots of locking/blocking)

## Trade-offs
### Pros:
- Protects data consistency with multiple users
- Provides flexibility: choose weaker isolation for performance or stronger for safety

### Cons:
- More locks = more contention
- Higher isolation = lower performance
- Deadlocks possible if lock ordering isn't managed

## Real World Examples
- **Read Committed**: Banking &rightarrow; to ensure you dont see uncommitted money transfers
- **Repeatable Read**: Inventory management &rightarrow; to prevent prices from changing mid-transaction
- **Serializable** Ticket booking &rightarrow; avoids to uses from booking the same seat.

#### Deadlock case
- Txn A: locks row in `Users`, needs  row in `Orders`
- Txn B: locks row in `Orders`, needs row in `Users`
- &rightarrow; Both wait forever until DB resolves (by killing one)

#### Interview case
*Explain isolation levels with examples of anomalies?*

## Diagram Idea
*e.g. timeline of two transactions &rightarrow; arros showing when reads/writes happen, highlighting anomalies at weaker isolation and how stronger levels prevent them*