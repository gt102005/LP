def knapsack(values,weights,capacity):
    dp = [[0 for i in range(capacity+1)] for j in range(len(values)+1)]

    for item in range(1,len(values) + 1):
        for weight in range(1,capacity + 1):
            if weights[item - 1] <= weight:
                dp[item][weight] = max(dp[item-1][weight-weights[item-1]]+values[item-1],dp[item-1][weight])
            else:
                dp[item][weight] = dp[item-1][weight]
    return dp[-1][-1]


while True:
    print("Press Ctrl+C to terminate...")
    n = int(input('Enter number of items: '))
    values = [int(i) for i in input("Enter values of items:").split(" ")]
    weights = [int(i) for i in input("Enter weights of items:").split(" ")]
    capacity = int(input("Enter maximum weight: "))
    maximum_value = knapsack(values,weights,capacity)
    print('The maximum value of items that can be carried:', maximum_value)



'''

🧠 Program Description

This Python program solves the 0/1 Knapsack Problem using a bottom-up Dynamic Programming (DP) approach.

The goal is to select items with given weights and values so that:

The total weight does not exceed the capacity of the knapsack.

The total value is maximized.

Each item can either be:
✅ Included (1)
❌ Excluded (0)
— hence called 0/1 Knapsack.

⚙️ How It Works
Function: knapsack(values, weights, capacity)

values: list of item values.

weights: list of item weights.

capacity: maximum weight the knapsack can carry.

The function builds a DP table where:

dp[i][w] = Maximum value that can be achieved using first i items with capacity w.

Step 1: Initialize DP Table
dp = [[0 for i in range(capacity+1)] for j in range(len(values)+1)]


Creates a 2D list of size (n+1) × (capacity+1), initialized with 0.

Rows → items (0 to n)

Columns → weights (0 to capacity)

Step 2: Fill DP Table

For each item i and each weight limit w:

Case 1: Item can fit

If weights[i-1] <= w:

dp[i][w] = max(
   value of including item i → dp[i-1][w - weights[i-1]] + values[i-1],
   value of excluding item i → dp[i-1][w]
)

Case 2: Item too heavy

If weights[i-1] > w:

dp[i][w] = dp[i-1][w]

Step 3: Return Result

The bottom-right cell of the table dp[-1][-1] contains the maximum achievable value.

Loop Section (Main Program)

The program runs in a loop allowing multiple test cases until terminated manually (Ctrl + C).

Takes number of items n

Takes values and weights of all items

Takes knapsack capacity

Calls the knapsack() function

Prints maximum value achievable

💻 Example Execution
Input:
Press Ctrl+C to terminate...
Enter number of items: 4
Enter values of items: 10 40 30 50
Enter weights of items: 5 4 6 3
Enter maximum weight: 10

DP Table Visualization:
Item	Weight	Value	Decision (for capacity=10)
1	5	10	Include (total = 10)
2	4	40	Include (total = 50)
3	6	30	Exclude
4	3	50	Replace items 1 & 2 → Include item 2 + 4 (total = 90)
Output:
The maximum value of items that can be carried: 90


✅ The optimal choice is to include item 2 (value=40, weight=4) and item 4 (value=50, weight=3).

🧮 Time and Space Complexity
Operation	Complexity	Explanation
Building DP table	O(n × W)	n = number of items, W = capacity
Space	O(n × W)	For the DP matrix
✅ Summary
Feature	Description
Algorithm Used	Dynamic Programming (Bottom-Up)
Problem Type	0/1 Knapsack
Input	Item values, item weights, knapsack capacity
Output	Maximum achievable value
Time Complexity	O(n × W)
Space Complexity	O(n × W)
Approach	Iterative DP (Tabulation)
⚙️ Sample Run Summary
Press Ctrl+C to terminate...
Enter number of items: 4
Enter values of items: 10 40 30 50
Enter weights of items: 5 4 6 3
Enter maximum weight: 10
The maximum value of items that can be carried: 90

'''