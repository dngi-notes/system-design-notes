# Acid Properties and Transactions

## Table of Contents
- [Acid Properties and Transactions](#acid-properties-and-transactions)
  - [Table of Contents](#table-of-contents)
  - [Purpose](#purpose)
  - [How it works](#how-it-works)
    - [1. Atomicity → All or Nothing](#1-atomicity--all-or-nothing)
    - [2. Consistency → Valid State Before and After](#2-consistency--valid-state-before-and-after)
    - [3. Isolation → Transactions Don't Interfere](#3-isolation--transactions-dont-interfere)
    - [4. Durability → Changes Survive Failure](#4-durability--changes-survive-failure)
  - [Trade-offs](#trade-offs)
    - [Pros](#pros)
    - [Cons](#cons)
  - [Real-World Examples](#real-world-examples)

## Purpose
Databases use transactions to group operations together so they behave like a single, reliable unit of work.
The **ACID** properties (Atomicity, Consistency, Isolation, Durability) guarantee data integrity even with crashes, errors or concurrent access (multiple users/processes) at once

## How it works
- **Transaction**: A sequence of operations treated as one logical unit (e.g. transfer €100 between accounts)
- **ACID** ensures transactions are:
### 1. Atomicity &rightarrow; All or Nothing
- Either the whole transactions completes or none of it does
- *Example: In a money transfer, if the debit succeeds but the credit fails, the whole transaction is rolled back*

### 2. Consistency &rightarrow; Valid State Before and After
- The database must always move from one valid state to another (respecting constraints/rules)
- *Example: A transfer shouldn't create/delete money.*

### 3. Isolation &rightarrow; Transactions Don't Interfere
- Each transaction behaves as if it is the only one running
- *Example: If two people are trying to buy the last available item at the same time, isolation ensures only one succeeds*

### 4. Durability &rightarrow; Changes Survive Failure
- Once committed, data is permanent (even in the case of failures/faults/crashes)
- *Example: After a successful bank transfer, the updated balances remain, even if the power goes out*

## Trade-offs
### Pros
- Guarantee data correctness and reliability
- Critical for financial, medical, and other safety-related systems
### Cons
- Performance overhead (locking, logging)
- May reduce throughput under heavy load
- Sometimes relaxed (BASE model, NoSQL) for scalability

## Real-World Examples
- **Banking**: Transfers, Deposits, Withdrawals
- **E-commerce**: Stock updates after a purchase
- **Ticketing systems**: Preventing double booking

**Interview**: Explain how ACID applies to money transfers between accounts