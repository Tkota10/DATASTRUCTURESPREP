class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        #Initialize an adjacency list that is initially an empty list
        #fill it with it's prereqs
        #Iterate through the numcourses
        #for each element, make a visited Set, and thhen for each time you run a DFS, pass a visited set that has zeroes.
        #If the element is a zero, than it hasn't been visited. If it's -1 it has been visited. If it's 1, than the course has alread finished.


        adj = [[] for i in range(numCourses)]
        res = []

        for pre, crs in prerequisites:
            adj[crs].append(pre)
        visited = [0] * numCourses

        def dfs(start, visited):
            if visited[start] == -1: #reach a node that has alread been visited in this DFS
                return False
            elif visited[start] == 1: #reach a node that has already been added into the output list
                return True
            visited[start] = -1

            for pre in adj[start]: #access the prereqs for the specificied course(We do this for each element we analyze in our NumCourses)
                if not dfs(pre, visited):
                    return False #Exists a circle
            res.append(start) #Permanently add this to our output
            visited[start] = 1 #Now for future DFS's we can automatically return True, when we reach that element. And we don't have to run more DFS to confirm if it's correct
            return True
                    
            

        for i in range(numCourses):
            if not dfs(i, visited):

                return []
        return res[::-1]