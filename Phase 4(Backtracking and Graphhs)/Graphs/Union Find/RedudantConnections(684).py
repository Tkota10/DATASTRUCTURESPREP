class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        #Ranks and parents list
        #All of the ranks (how many elements are in that list)
        #Parents of that list

        parent = [i for i in range(len(edges) + 1)]
        
        def find(x):
            if parent[x] != x: #If it's not just a standalone graph by itself. If it is you can just immediately return x
                parent[x] = find(parent[x]) #Find the parent[x] by the recursion with the find () call/ This iteration is created to find the root parent. This is the same as parent[x] = parent[parent[x]]
            return parent[x]

        def union(p, q):
            up, uq = find(p), find(q)

            if up == uq:
                return False
            
            #Change the parent variable
            parent[uq] = up # Set the parent of uq to be up

            return True
        
        for edge1, edge2 in edges:
            if not union(edge1, edge2):
                return [edge1, edge2]