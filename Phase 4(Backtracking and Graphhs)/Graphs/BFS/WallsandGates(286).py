import collections
class Solution(object):
    def wallsAndGates(self, rooms):

        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """


        #Nested for loops to find all the gates

        #Then a BFS search to calucate the distance from all of these gates. Increment by 1, until you reach the edge or output.

        q = collections.deque()

        if not rooms:
            return []
        #Identify all the gates

        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    q.append((i, j))
        

        dirs = [(-1,0),(0,-1),(1,0),(0,1)]
        #Create distances from gates
        while q:
            x, y = q.popleft()
            distance = rooms[x][y] + 1

            for dx, dy in dirs:
                new_x, new_y = x + dx, y + dy
                # If it's an empty row and on the board
                if 0<=new_x<len(rooms) and 0<=new_y<len(rooms[0]) and rooms[new_x][new_y] == 2147483647:
                    rooms[new_x][new_y] = distance
                    q.append((new_x, new_y))
        return rooms