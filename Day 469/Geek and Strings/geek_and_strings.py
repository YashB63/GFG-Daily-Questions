class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.cnt = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True
        cur.cnt += 1


class Solution:
    def prefixCount(self, N, Q, words, query):
        trie = Trie()

        for word in words:
            trie.insert(word)

        res = []
        items = {}

        for q in query:
            cur = trie.root
            idx = 0
            if q in items:
                res.append(items[q])
                continue
            while idx < len(q) and q[idx] in cur.children:
                cur = cur.children[q[idx]]
                idx += 1

            if len(q) != idx:
                res.append(0)
            else:
                stack = [cur]
                vis = set()
                vis.add(cur)
                path = q
                total = 0
                while stack:
                    top= stack[-1]
                    found = False
                    for key,node in top.children.items():
                        if node not in vis:
                            vis.add(node)
                            stack.append(node)
                            found = True
                            path += key
                            break
                    if not found:
                        pop = stack.pop()
                        if pop.isWord:
                            total += pop.cnt
                        path = path[:-1]
                res.append(total)
                items[q] = total
        return res