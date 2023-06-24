class TrieNode:
    def __init__(self):
        self.children = {}
        self.endof = False

class Trie(object):

    def __init__(self):
     self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur = self.root
        #Inserts the word, If that character is not already there, then it add to children matrix. 
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endof = True


        #Tarun thinking out loud:
        #Goes one by one by character and if it's seen in the prefix, it keeps on moving on
        #Then if it reaches an empty state, add a element and keep on going. Than once it reaches the last element, add that element. and set the 'endof' to be False
        

    def search(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endof #This is because whatever the last element is, if the endof is True
        """
        :type word: str
        :rtype: bool
        """
        

    def startsWith(self, prefix):
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True

        """
        :type prefix: str
        :rtype: bool
        """
        

