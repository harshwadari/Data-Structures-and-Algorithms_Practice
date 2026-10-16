"""
Trie (prefix Tree):

A Trie is a tree-based Advanced data structure used to store and search strings
efficiently, especially when the strings have common prefixes.

Why do we use Trie?
- Fast word searching
- Fast prefix searching
- Useful for autocomplete
- Useful for dictionary/word problems

Example:
"cat", "car", "can" share the common prefix "ca".
"""


"""
Advanced Data Structures
│
├── 1. Trie
│   ├── Insertion
│   ├── Searching
│   ├── Prefix Search
│   └── Bitwise Trie
│
├── 2. Fenwick Tree (Binary Indexed Tree)
│   ├── Prefix Sum Queries
│   └── Point Updates
│
└── 3. Segment Tree
    ├── Range Queries
    ├── Point Updates
    └── Lazy Propagation
"""





class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    # Insert word into trie
    # TC = O(N)
    def insert(self,word:str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True
    # search word
    # TC = O(N)
    def search(self,word:str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.isEnd 
    # search for prefix
    # TC = O(N)
    # SC = O(N) for dicitonary 
    def startswith(self,prefix:str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
trie = Trie()
trie.insert("apple")
trie.insert("apps")
print(trie.search("app"))
print(trie.startswith('ap'))