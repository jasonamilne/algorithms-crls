# Detailed Explanation of Loop Invariant Maintenance in Linear Search

## The Maintenance Property
The maintenance property proves that if the loop invariant is true before an iteration, it remains true before the next iteration.

## Loop Invariant Statement
"At the start of each iteration, the subarray A[0..i-1] has been searched, and the value has not been found in any of these positions."

## Important Note About Array Indexing
The loop invariant states: "A[0..i-1] has been searched" where i is the current iteration.
- When i = 0: A[0..-1] = empty array (initialization)
- When i = 1: A[0..0] = first element searched
- When i = 2: A[0..1] = first two elements searched

## Proof of Maintenance

### Starting Assumption
Let's assume our loop invariant holds for iteration k:
- We have searched all elements in A[0..k-1]
- We know value is not in any position from 0 to k-1
- We are about to examine A[k]

### Step-by-Step Analysis

1. At position k, exactly one of two things happens:

   **Case 1: A[k] equals value**
   ```python
   if A[k] == value:
       return k    # We found it! Algorithm terminates
   ```
   - The algorithm terminates immediately
   - No need to maintain invariant further

   **Case 2: A[k] does not equal value**
   ```python
   # implicit else - we continue to next iteration
   ```
   - We now know value is not in A[k]
   - Combined with our invariant:
     * value is not in A[0..k-1] (from invariant)
     * value is not in A[k] (just checked)
     * Therefore, value is not in A[0..k]

### Maintenance Conclusion
When we move to iteration k+1:
- Our invariant must hold for A[0..k]
- We just proved value isn't in A[0..k]
- This matches exactly what we need for iteration k+1
- Therefore, the maintenance property holds

### Example with A = [1,3,70,4], value = 70
Showing maintenance at each step:

1. k = 0:
   - Invariant: [] is searched (true)
   - Check A[0] = 1 ≠ 70
   - New invariant: [1] is searched, no 70 found

2. k = 1:
   - Invariant: [1] is searched, no 70 found (true)
   - Check A[1] = 3 ≠ 70
   - New invariant: [1,3] is searched, no 70 found

3. k = 2:
   - Invariant: [1,3] is searched, no 70 found (true)
   - Check A[2] = 70 = 70
   - Algorithm terminates, maintenance property held until termination
