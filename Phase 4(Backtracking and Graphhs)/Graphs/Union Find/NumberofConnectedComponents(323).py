class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """


        #Find function

        #Union Function

        #Keep on adding as many you can

        parent = [i for i in range(n)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union (x, y):
            ux, uy = find(x), find(y)

            if ux == uy:
                return False
            
            parent[uy] = ux
            
            
            return True
        
        res = n
        for edge1, edge2 in edges:
            if union(edge1, edge2):
                res -= 1
        return res
            