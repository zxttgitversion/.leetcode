#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        self._dfs(word, 0, self.root)

    def _dfs(self, word: str, index: int, node: TrieNode) -> bool:
        if index == len(word):
            return node.is_end
        
        ch = word[index]
        if ch == '.':
            for child in node.children.values():
                if self._dfs(word, index + 1, child):
                    return True
                return False
        else:
            if ch not in node.children:
                return False
            return self._dfs(word, index + 1, node.children[ch])


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

