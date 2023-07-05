class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """


        def dfs(board, i, j, word):
            
            #we have found all the elements in the graph
            if len(word) == 0:
                return True

            #If it breaks on of the edge cases
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
                return False
            
            #Marking off a variable has already seen
            tmp = board[i][j]
            board[i][j] = '#'

            #we want to run dfs searches on all 4 corners

            res = dfs(board, i + 1, j, word[1:]) or dfs(board, i - 1, j, word[1:]) or dfs(board, i, j + 1, word[1:]) or dfs(board, i, j - 1, word[1:])

            #We have to update the element back to what it was before after we change it

            board[i][j] = tmp
            return res
        
        #Checking if the board is empty
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(board, i, j, word):
                    return True
        return False
