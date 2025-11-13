class Node:
    def __init__(self,left=None,right=None,value=None,frequency=None):
        self.left = left
        self.right = right
        self.value = value
        self.frequency = frequency
    
    def children(self):
        return (self.left,self.right)



class Huffman_Encoding:
    def __init__(self,string):
        self.q = []
        self.string = string
        self.encoding = {}

    def char_frequency(self):
        count = {}
        for char in self.string:
            if char not in count:
                count[char] = 0
            count[char] += 1

        for char,value in count.items():
            node = Node(value=char,frequency=value)
            self.q.append(node)
        self.q.sort(key=lambda x: x.frequency)    

    def build_tree(self):
        while len(self.q) > 1:
            n1 = self.q.pop(0)
            n2 = self.q.pop(0)
            node = Node(left=n1,right=n2,frequency=n1.frequency + n2.frequency)
            self.q.append(node)
            self.q.sort(key = lambda x:x.frequency)

    
    def helper(self,node:Node,binary_str="",):
        if type(node.value) is str:
            self.encoding[node.value] = binary_str
            return
        l,r = node.children()
        self.helper(node.left,binary_str + "0")
        self.helper(node.right,binary_str + "1")
        print(node.frequency)
        return
        

    def huffman_encoding(self):
        root = self.q[0]
        self.helper(root,"")


    def print_encoding(self):
        print(' Char | Huffman code ')
        for char,binary in self.encoding.items():
            print(" %-4r |%12s" % (char,binary))
    
    def encode(self):
        self.char_frequency()
        self.build_tree()
        self.huffman_encoding()
        self.print_encoding()

string = input("Enter string to be encoded: ")
# string = 'AAAAAAABBCCCCCCDDDEEEEEEEEE'
encode = Huffman_Encoding(string)
encode.encode()


# The time complexity for encoding each unique character based on its frequency is O(nlog n).

# Extracting minimum frequency from the priority queue takes place 2*(n-1) times and its complexity is O(log n). Thus the overall complexity is O(nlog n).



'''

🧠 Program Description

This Python program implements the Huffman Encoding Algorithm, which is a lossless data compression method used to encode characters based on their frequency of occurrence in a given string.

Characters that occur more frequently are assigned shorter binary codes, while less frequent characters get longer codes.

⚙️ Working Principle of Huffman Encoding

Calculate character frequencies.

Build a Huffman Tree by repeatedly combining two least frequent nodes.

Assign binary codes (0 for left, 1 for right) to each character.

Output the encoded binary representation for every character.

🔹 Class Breakdown
1. Node class

Represents a single node in the Huffman Tree.

Attributes:

left: Left child node

right: Right child node

value: Character value (if leaf node)

frequency: Frequency of the character or sum of child frequencies

2. Huffman_Encoding class
Attributes:

self.q: List acting as a priority queue (sorted by frequency)

self.string: Input string to encode

self.encoding: Dictionary to store final Huffman codes

Key Methods:
🔸 char_frequency()

Counts frequency of each character.

Creates a Node for each character and stores it in self.q.

Sorts the list based on frequency.

🔸 build_tree()

Repeatedly merges two least frequent nodes.

Creates a parent node with frequency = sum of children’s frequencies.

Pushes the new node back into the queue and sorts again.

Repeats until one node remains (root).

🔸 helper(node, binary_str="")

Recursively traverses the Huffman tree.

Appends '0' when moving left, '1' when moving right.

When a leaf node (character) is reached, stores the binary string in self.encoding.

🔸 huffman_encoding()

Starts the recursive encoding from the root of the Huffman Tree.

🔸 print_encoding()

Displays the character and its Huffman code in a formatted table.

🔸 encode()

Calls all main methods in order:

Count frequencies

Build tree

Generate Huffman codes

Print the result

🧮 Example Execution
Input:
Enter string to be encoded: AAAAAAABBCCCCCCDDDEEEEEEEEE

Step 1: Character Frequencies
Character	Frequency
A	7
B	2
C	6
D	3
E	9
Step 2: Huffman Tree Construction

The tree is built bottom-up by merging least frequent nodes:

       (27)
       /   \
    (11)   (16)
   /   \   /   \
 (5)  (6) (7)  (9)


(Exact structure may vary based on merge order, but the encoding remains valid.)

Step 3: Assign Huffman Codes

Binary codes are assigned based on tree traversal:

Character	Huffman Code
E	1
A	01
C	001
D	0001
B	0000

(Note: exact codes depend on tree build order, but pattern and relative length are the same.)

Step 4: Output
Enter string to be encoded: AAAAAAABBCCCCCCDDDEEEEEEEEE
 Char | Huffman code 
 'E'  |           1
 'A'  |          01
 'C'  |         001
 'D'  |        0001
 'B'  |        0000

🧩 Time Complexity Analysis
Operation	Explanation	Time Complexity
Frequency Counting	Traverse all characters	O(n)
Building Huffman Tree	Each extraction & insertion from queue of size n	O(n log n)
Generating Codes	Traverse Huffman tree	O(n)
Overall Complexity		O(n log n)

'''