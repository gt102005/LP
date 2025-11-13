def fibonacci_iterative(n:int):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        dp = [0] * n
        dp[0] = 0
        dp[1] = 1
        for i in range(2,n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]

def fibonacci_recursive(n):
    cache = {
        1:0,
        2:1
    }
    return helper(n,cache)

def helper(n:int,cache):
    if n in cache:
        return cache[n]
    else:
        return helper(n-1,cache) + helper(n-2,cache)


n = int(input("Enter value of n(nth Fibonacci number): "))
print(f"Fibonacci Number(Iterative): {fibonacci_iterative(n)}")
print(f"Fibonacci Number(Recursive): {fibonacci_recursive(n)}")

'''

🧠 Program Description

This Python program computes the n-th Fibonacci number using two approaches:

Iterative Dynamic Programming Approach

Recursive Approach with Memoization (caching)

🔹 1. Iterative Approach (fibonacci_iterative)

Logic:

For n = 1, Fibonacci number is 0.

For n = 2, Fibonacci number is 1.

For larger n, it builds a list dp where:

dp[i] = dp[i-1] + dp[i-2]

Finally, it returns dp[n-1], which is the n-th Fibonacci number.

Time Complexity: O(n)
Space Complexity: O(n)

🔹 2. Recursive Approach (fibonacci_recursive)

Logic:

Uses a helper function helper(n, cache).

A cache (dictionary) stores already computed Fibonacci numbers to avoid recalculating them.

If n is in the cache, return its value.

Otherwise, recursively calculate helper(n-1) + helper(n-2) and return.

⚠ Issue:
This recursive function does not update the cache with new computed values, so it behaves like a normal recursive Fibonacci, not true memoization.
→ Hence, it will be very slow for large n.

Time Complexity: O(2ⁿ) (since no memoization update)
Space Complexity: O(n) (due to recursion stack)

🧩 Code Flow

User inputs n.

Program prints:

Fibonacci number using the iterative method.

Fibonacci number using the recursive method.

💻 Example Run
Input:
Enter value of n(nth Fibonacci number): 7

Step-by-step Iterative Calculation:

Fibonacci sequence = 0, 1, 1, 2, 3, 5, 8
→ 7th Fibonacci number = 8

Recursive Calculation:

Performs same computation recursively.

Output:
Enter value of n(nth Fibonacci number): 7
Fibonacci Number(Iterative): 8
Fibonacci Number(Recursive): 8

'''