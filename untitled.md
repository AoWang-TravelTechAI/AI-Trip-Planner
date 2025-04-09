# Homework 4 Solutions  
**Course:** CS101 Algorithms  
**Student:** Ao Wang (20033397)  
**Date:** March 25, 2025  

---

## Problem 1: Recursive Cases for Divide-and-Conquer AB-Search
The three possible cases when dividing the problem:

1. **Left Half Case**:  
   `ab` appears entirely in the left half → `ab_search(data[1..mid], mid)`

2. **Right Half Case**:  
   `ab` appears entirely in the right half → `ab_search(data[mid+1..n], n - mid)`

3. **Cross-Boundary Case**:  
   `data[mid] == 'a' && data[mid+1] == 'b'` (spans the midpoint)

---

## Problem 2: Base Cases
The base conditions for termination:
```python
if n < 2: 
    return -1  # Too short to contain 'ab'
if data[0] == 'a' and data[1] == 'b':
    return 0   # Found at beginning

---

def ab_search(data, n):
    """Finds first 'ab' substring using divide-and-conquer"""
    # Base cases
    if n < 2:
        return -1
    if data[0] == 'a' and data[1] == 'b':
        return 0
    
    mid = n // 2
    
    # Check cross-boundary case
    if mid > 0 and data[mid-1] == 'a' and data[mid] == 'b':
        return mid - 1
    
    # Recursive cases
    left = ab_search(data[:mid], mid)
    if left != -1:
        return left
        
    right = ab_search(data[mid:], n - mid)
    if right != -1:
        return mid + right
    
    return -1  # Not found

---

def min_squares(n):
    if n == 0: return 0
    min_cnt = float('inf')
    for i in range(1, int(n**0.5)+1):
        min_cnt = min(min_cnt, 1 + min_squares(n-i*i))
    return min_cnt