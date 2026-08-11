# Secure Maximum Deliveries

## Problem Statement

As a logistics manager in an automobile manufacturing company, you are responsible for storing deliveries in secure warehouses.

You are given an integer array `deliveryLogs` of size `n`, where each element represents the number of parts delivered in the `i`-th encrypted delivery log.

You are also given an even integer `k`, representing the number of secure warehouses available.

## When Deliveries Are Stored

- Each warehouse can store deliveries taken from a **single delivery log only**.
- Deliveries from different logs **cannot be mixed** in the same warehouse.
- Deliveries from a single log **may be split across multiple warehouses**.
- After storing, exactly `k/2` warehouses having the **largest number of deliveries** become compromised.
- The remaining `k/2` warehouses are safe.
- Only deliveries stored in the safe warehouses are counted as secure.

## Task

Find the **maximum number of secure deliveries** that can be stored.

---

## Example

```text
n = 4
deliveryLogs = [3, 5, 9, 6]
k = 4
```

If all deliveries from each log are decoded and stored separately:

```text
Warehouse 1 -> 3
Warehouse 2 -> 5
Warehouse 3 -> 9
Warehouse 4 -> 6
```

The two warehouses with the largest number of deliveries (`9` and `6`) are compromised.

Therefore:

```text
secure = 3 + 5 = 8
```

However, we can distribute the deliveries differently:

1. Decrypt all deliveries in the second log and store them in the first warehouse.
2. Decrypt four deliveries from the third log and store them in the second warehouse.
3. Decrypt the remaining five deliveries from the third log and store them in the third warehouse.
4. Decrypt all deliveries in the fourth log and store them in the fourth warehouse.

This gives warehouse sizes:

```text
[5, 4, 5, 6]
```

The two largest warehouses (`6` and `5`) are compromised.

The remaining two warehouses contain:

```text
4 + 5 = 9
```

Therefore, the answer is:

```text
9
```

---

## Function Description

Complete the function:

```python
secureMaximumDeliveries(deliveryLogs, k)
```

### Parameters

`deliveryLogs`

```text
int deliveryLogs[n]
```

The number of deliveries in the `i`-th encrypted log.

`k`

```text
int k
```

The number of secure warehouses available.

### Returns

```text
int
```

The maximum number of secure deliveries you can make.

---

## Constraints

- `1 <= n <= 1000`
- `2 <= k <= 1000`
- `0 <= deliveryLogs[i] <= 1000`
- `k` is guaranteed to be an even integer.

---

# Sample Case 0

### Input

```text
n = 1
deliveryLogs = [6]
k = 2
```

### Output

```text
3
```

### Explanation

There are two warehouses.

Split the 6 deliveries equally:

```text
Warehouse 1 -> 3
Warehouse 2 -> 3
```

Both warehouses have 3 deliveries.

One of them will be compromised because exactly `k/2 = 1` warehouse is compromised.

The other warehouse is safe.

Therefore:

```text
answer = 3
```

---

# Sample Case 1

### Input

```text
n = 6
deliveryLogs = [5, 5, 5, 5, 5, 5]
k = 4
```

### Output

```text
10
```

### Explanation

Store the logs separately:

```text
[5, 5, 5, 5, 5, 5]
```

We only need four warehouses, so use four of them:

```text
[5, 5, 5, 5]
```

Exactly `k/2 = 2` warehouses with the largest number of deliveries are compromised.

Two warehouses remain safe:

```text
5 + 5 = 10
```

Therefore:

```text
answer = 10
```

---

## Important Observation

The key restriction is:

> **A single log can be split among multiple warehouses, but one warehouse cannot contain deliveries from multiple logs.**

This is what makes the problem different from a straightforward array partitioning problem.

## Main Example

```text
deliveryLogs = [3, 5, 9, 6]
k = 4

Answer = 9
```
