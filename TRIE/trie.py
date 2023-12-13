class trie_node:
    def __init__(self) -> None:
        self.children ={}
        self.is_word=False
class trie:
    def __init__(self) -> None:
        self.root=trie_node()
    def insert(self,word):
        node=self.root
        for char in word:
            if char not in node.children:
                node.children[char]=trie_node()
            node=node.children[char]
        node.is_word=True
    def search(self,word):
        node=self.root
        for char in word:
            if char not in node.children:
                return False
            node=node.children[char]
        return node.is_word
    def starts_with(self,prefix):
        node=self.root
        for char in prefix:
            if char not in node.children:
                return False
            node=node.children[char]
        return True
t1=trie()
t1.insert("pooja")
t1.insert("apple")
t1.insert("orange")
t1.insert("banana")
t1.insert("app")
print(t1.search("pooja"))
print(t1.search("ss"))
print(t1.starts_with("a"))
print(t1.starts_with("j"))