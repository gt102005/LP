def knapsack_01(n, values, weights, W):
    dp = [[0] * (W+1) for _ in range(n+1)]

    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    
    selected_items = []
    i, w = n, W
    while i > 0 and w > 0:
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i-1)
            w -= weights[i-1]
        i -= 1
    
    return dp[n][W], selected_items

if __name__ == "__main__":
    n = 3
    values = [60, 100, 120]
    weights = [10, 20, 30]
    W = 50

    max_value, selected_items = knapsack_01(n, values, weights, W)
    print("Maximum value:", max_value)
    print("Selected items:", selected_items)
    

'''

🧠 PROGRAM DESCRIPTION
============================================================

This Python program demonstrates the **0/1 Knapsack Problem** using 
**Dynamic Programming** and **item tracking** to determine:

1️⃣ The maximum total value achievable without exceeding the knapsack’s weight capacity.  
2️⃣ Which specific items make up that optimal solution.

------------------------------------------------------------
⚙️ HOW THE 0/1 KNAPSACK ALGORITHM WORKS
------------------------------------------------------------

The 0/1 Knapsack is a classic optimization problem that follows a bottom-up 
Dynamic Programming approach.

For each item and each possible capacity W, the algorithm decides whether to:

• **Include** the item → add its value to the best value of remaining capacity.  
• **Exclude** the item → keep the previous best value for the same capacity.  

The decision is made using:
   dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])

After filling the DP table, the maximum value is found at `dp[n][W]`.  
Backtracking through the table reveals which items were selected.

------------------------------------------------------------
🔹 FUNCTION BREAKDOWN (knapsack_01)
------------------------------------------------------------

1. **Initialization**
   • Creates a DP table of size (n + 1) × (W + 1) initialized to 0.  
   • Each row represents items 1 → n; each column represents capacity 0 → W.  

2. **Building the DP Table**
   • Iterates over each item and capacity.  
   • If current item fits in capacity (w ≥ weights[i-1]), update the cell using:  
        dp[i][w] = max(dp[i-1][w], dp[i-1][w - weights[i-1]] + values[i-1])  
   • Otherwise, copy the previous row’s value (dp[i-1][w]).

3. **Backtracking Phase**
   • Starts from bottom-right corner (dp[n][W]).  
   • If `dp[i][w] != dp[i-1][w]`, it means item (i-1) was included.  
   • Reduce w by that item’s weight and continue until i = 0 or w = 0.  

4. **Return Results**
   • Maximum value (dp[n][W])  
   • List of selected item indices (selected_items)

------------------------------------------------------------
💻 EXAMPLE EXECUTION
------------------------------------------------------------
Input Data:
n = 3  
values = [60, 100, 120]  
weights = [10, 20, 30]  
W = 50  

Step by step:
• Item 1 (weight 10, value 60) fits → include it.  
• Item 2 (weight 20, value 100) fits → better value.  
• Item 3 (weight 30, value 120) also fits → combine with item 2 for best total.  

Output:
------------------------------------------------------------
Maximum value: 220  
Selected items: [2, 1]
------------------------------------------------------------

Explanation:
Items 1 and 2 (0-based indices) yield the maximum value 220 within capacity 50.  
Order of indices is reversed because we backtrack from the bottom of the table.

------------------------------------------------------------
⏱ TIME COMPLEXITY ANALYSIS
------------------------------------------------------------
Case         Time Complexity      Space Complexity  
Best / Average / Worst  → O(n × W)       O(n × W)

------------------------------------------------------------
🔸 WHY DYNAMIC PROGRAMMING FOR KNAPSACK?
------------------------------------------------------------
• Naive recursion explores every combination → O(2ⁿ).  
• DP reuses previous results (subproblems) → much faster.  
• Efficiently handles large inputs with bounded weights.  

------------------------------------------------------------
✅ PROGRAM PURPO

'''