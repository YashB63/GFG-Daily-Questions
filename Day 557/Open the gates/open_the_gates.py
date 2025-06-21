SIZE = 26

class TrieNode():

    def __init__(self):
        self.leaf = False
        self.child = [None] * SIZE
        for i in range(SIZE):
            self.child[i] = None

class Solution():

    def insert(self, root, key):

        n = len(key)
        pChild = root

        for i in range(n):
            index = ord(key[i]) - ord('A')
            if pChild.child[index] == None:
                pChild.child[index] = TrieNode()

            pChild = pChild.child[index]

        pChild.leaf = True

    def isSafe(self, i, j, visited):
        if i >= 0 and i < self.M and j >= 0 and j < self.N and visited[i][
                j] == False:
            return True
        return False

    def searchWord(self, root, boggle, i, j, visited, s, fans):
        if root.leaf == True:
            fans.add(s)

        if self.isSafe(i, j, visited):
            visited[i][j] = True

            for k in range(SIZE):
                if root.child[k] != None:
                    ch = chr(k + ord('A'))

                    if self.isSafe(i + 1, j + 1,
                                   visited) and boggle[i + 1][j + 1] == ch:
                        self.searchWord(root.child[k], boggle, i + 1, j + 1,
                                        visited, s + ch, fans)

                    if self.isSafe(i, j + 1,
                                   visited) and boggle[i][j + 1] == ch:
                        self.searchWord(root.child[k], boggle, i, j + 1,
                                        visited, s + ch, fans)

                    if self.isSafe(i - 1, j + 1,
                                   visited) and boggle[i - 1][j + 1] == ch:
                        self.searchWord(root.child[k], boggle, i - 1, j + 1,
                                        visited, s + ch, fans)

                    if self.isSafe(i + 1, j,
                                   visited) and boggle[i + 1][j] == ch:
                        self.searchWord(root.child[k], boggle, i + 1, j,
                                        visited, s + ch, fans)

                    if self.isSafe(i + 1, j - 1,
                                   visited) and boggle[i + 1][j - 1] == ch:
                        self.searchWord(root.child[k], boggle, i + 1, j - 1,
                                        visited, s + ch, fans)

                    if self.isSafe(i, j - 1,
                                   visited) and boggle[i][j - 1] == ch:
                        self.searchWord(root.child[k], boggle, i, j - 1,
                                        visited, s + ch, fans)

                    if self.isSafe(i - 1, j - 1,
                                   visited) and boggle[i - 1][j - 1] == ch:
                        self.searchWord(root.child[k], boggle, i - 1, j - 1,
                                        visited, s + ch, fans)

                    if self.isSafe(i - 1, j,
                                   visited) and boggle[i - 1][j] == ch:
                        self.searchWord(root.child[k], boggle, i - 1, j,
                                        visited, s + ch, fans)

            visited[i][j] = False

    def findWords(self, boggle, root):
        self.M = len(boggle)
        self.N = len(boggle[0])
        visited = [[False for i in range(self.N)] for i in range(self.M)]

        pChild = root

        s = ""
        fans = set()

        for i in range(self.M):
            for j in range(self.N):
                index = ord(boggle[i][j]) - ord('A')
                if (pChild.child[index] != None):
                    s = s + boggle[i][j]
                    self.searchWord(pChild.child[index], boggle, i, j, visited,
                                    s, fans)
                    s = ""

        ans = []
        for el in fans:
            ans.append(el)
        return ans

    def wordBoggle(self, boggle, dictionary):
        root = TrieNode()
        n = len(dictionary)
        for i in range(n):
            self.insert(root, dictionary[i])

        return self.findWords(boggle, root)