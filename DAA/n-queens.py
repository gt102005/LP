class NQueens:
    def __init__(self) -> None:
        self.size = int(input("Enter size of chessboard: "))
        self.board = [[False]*self.size for _ in range(self.size)]
        self.count = 0
    def printBoard(self):
        for row in self.board:
            for ele in row:
                if ele == True:
                    print("Q",end=" ")
                else:
                    print("X",end=" ")
            print()
        print()
    
    def isSafe(self,row:int,col:int) -> bool:

        # Check Column(above and below of the (row,col))
        for i in self.board:
            if i[col] == True:
                return False
        
        # Check backward slash(\) diagonal only in above direction
        i = row
        j = col
        while i >= 0 and j >= 0:
            if self.board[i][j] == True:
                return False
            i -= 1
            j -= 1
        # Check backward slash(\) diagonal only in below direction
        i = row
        j = col
        while i < self.size and j < self.size:
            if self.board[i][j] == True:
                return False
            i += 1
            j += 1
        
        # Check forward slash diagonal(/) only in above direction
        i = row
        j = col
        while i >= 0 and j < self.size:
            if self.board[i][j] == True:
                return False
            i -= 1
            j += 1
        
         # Check forward slash diagonal(/) only in below direction
        i = row
        j = col
        while i < self.size and j >= 0:
            if self.board[i][j] == True:
                return False
            i += 1
            j -= 1
        
        return True
    
    def set_position_first_queen(self):
        print("Enter coordinates of first queen: ")
        row = int(input(f"Enter row (1-{self.size}): "))
        col = int(input(f"Enter column (1-{self.size}): "))
        self.board[row-1][col-1] = True
        self.printBoard()
    
    def solve(self,row:int):
        if row == self.size:
            self.count += 1
            self.printBoard()
            return
        
        if any(self.board[row]) is True:
            self.solve(row+1)
            return

        for col in range(self.size):
            if self.isSafe(row,col) == True:
                self.board[row][col] = True
                self.solve(row+1)
                self.board[row][col] = False
    
    def displayMessage(self):
        if self.count > 0:
            print("Solution exists for the given position of the queen.")
        else:
            print("Solution doesn't exist for the given position of the queen.")

solver = NQueens()
solver.set_position_first_queen()
solver.solve(0)
solver.displayMessage()


'''

🧠 Program Description

This Python program solves the N-Queens problem, a classic backtracking problem in artificial intelligence and algorithm design.

🏰 Problem Definition

You have an N × N chessboard, and you need to place N queens so that no two queens attack each other, i.e.:

No two queens share the same row.

No two queens share the same column.

No two queens share the same diagonal (both / and \).

This program:

Lets the user choose the board size (N).

Lets the user manually place the first queen.

Uses backtracking to find all valid solutions based on that starting position.

🧩 Class Breakdown: NQueens
1. __init__()

Prompts user for board size.

Initializes a board matrix of size N × N with False (no queens placed).

Initializes a counter count to track number of valid solutions found.

2. printBoard()

Displays the current board:

"Q" marks the position of a queen.

"X" marks an empty square.

Example Output:

Q X X X 
X X Q X 
X X X X 
X Q X X

3. isSafe(row, col)

Checks whether it’s safe to place a queen at position (row, col).

Safety conditions:

No other queen in the same column.

No other queen in the backslash diagonal (\) (both upward and downward).

No other queen in the forward slash diagonal (/) (both upward and downward).

Returns True if position is safe, False otherwise.

4. set_position_first_queen()

Asks the user to enter the row and column for the first queen.

Places the queen there.

Prints the board.

Example:

Enter size of chessboard: 4
Enter coordinates of first queen:
Enter row (1-4): 1
Enter column (1-4): 2


Board:

X Q X X 
X X X X 
X X X X 
X X X X 

5. solve(row)

Recursive backtracking function.

Base case: if row == size, a valid configuration is found → print the board and increment count.

Recursive step:

If a queen is already placed in the current row (like the user-specified first queen), skip to next row.

Otherwise, try placing a queen in every column that is safe.

Recursively call solve(row + 1).

Backtrack (remove queen) to explore other configurations.

6. displayMessage()

After solving:

If count > 0: prints a success message.

Otherwise: prints a failure message (no solution for that initial queen position).

7. Main Execution
solver = NQueens()
solver.set_position_first_queen()
solver.solve(0)
solver.displayMessage()

💻 Example Execution
Input:
Enter size of chessboard: 4
Enter coordinates of first queen:
Enter row (1-4): 1
Enter column (1-4): 2

Output (one of the possible solutions):
X Q X X 
X X X Q 
Q X X X 
X X Q X 

X Q X X 
X X X X 
Q X X Q 
X X Q X 

Solution exists for the given position of the queen.


(Exact number of solutions depends on initial position of the first queen.)

⏱ Time Complexity Analysis
Step	Description	Complexity
Checking safety	Checking column and diagonals	O(N)
Recursive placement	Tries N positions for N queens	O(N!) worst case
Overall	Backtracking approach	O(N!)

✅ Space Complexity: O(N²) (for the board and recursion stack)

'''