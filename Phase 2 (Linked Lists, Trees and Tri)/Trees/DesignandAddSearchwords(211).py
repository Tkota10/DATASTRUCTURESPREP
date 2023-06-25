class WordNode:
    def __init__(self):
        self.children = {}
        self.endof = False

class WordDictionary(object):

    def __init__(self):
        self.root = WordNode()
        

    def addWord(self, word):

        #For character in the element
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = WordNode()
            cur = cur.children[c]
        cur.endof = True

        """
        :type word: str
        :rtype: None
        """
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def dfs(j, root):
            cur = root
            for i in range(j, len(word)):

                c = word[i]

                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False


                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.endof

        return dfs(0, self.root)
            