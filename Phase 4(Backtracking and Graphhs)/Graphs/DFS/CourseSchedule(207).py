class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        #Inputs: numCourses, prerquisites

        #Thought processes
        #We want to dertmine the graphs

        #create a hashmap of course with their prereqs

        #Make a adjanency list of all the prereqs

        preMap = {i:[] for i in range(numCourses)}

        #preMap = [[], [], [], [], []] 


        for crs, pre in prerequisites:
            preMap[crs].append(pre)
            #prerequisites = [('B', 'A'), ('C', 'A'), ('C', 'B')]
            #premap = {'B': ['A'], 'C': ['A', 'B']}

        #visitSet (Stuff that we've already visited along curr DFS Pathh)

        visitSet = set()
        def dfs(crs):
            #If it's in visit
            if crs in visitSet:
                return False
            #empty list, course has no prereqs and is the end of thhe list
            if preMap[crs] == []:
                return True
            
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                     return False #If there's a false, than we can call it false immediately.
            visitSet.remove(crs) #Remove the root node (from the visited list)/ #Resets the visitSet
            preMap[crs] = []
            return True
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
        