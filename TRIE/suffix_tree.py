class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_suffix(self, suffix):
        node = self.root
        for char in reversed(suffix):
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search_suffix(self, suffix):
        node = self.root
        for char in reversed(suffix):
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Example usage:
s = Trie()
s.insert_suffix("apple")
s.insert_suffix("banana")
s.insert_suffix("orange")

print(s.search_suffix("le"))  
print(s.search_suffix("poo"))  
print(s.search_suffix("ge"))   
