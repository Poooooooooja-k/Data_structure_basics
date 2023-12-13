class trie_node:
    def __init__(self) -> None:
        self.children={}
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
    def get_suggestions(self,prefix):
        node=self.root
        for char in prefix:
            if char not in node.children:
                return[]
            node=node.children[char]
        suggestions=[]
        self.dfs(node,prefix,suggestions)
        return suggestions
    def dfs(self,node,prefix,suggestions):
        if node.is_word:
            suggestions.append(prefix)
        for char,child_node in node.children.items():
            self.dfs(child_node,prefix+char,suggestions)

trie1 = trie()
trie1.insert("pooja")
trie1.insert("apple")
trie1.insert("banana")
trie1.insert("orange")
trie1.insert("app")
trie1.insert("application")
suggestions = trie1.get_suggestions("app")
print(suggestions) 




