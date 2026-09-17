# https://leetcode.com/problems/01-matrix/

# BFS solution iterative approach using queue. Using the size variable and updating dist. 
# This logic starts by checking for 1. 
# TC: O(m^2*n^2)
# SC: O(m*n) + O(m*n)n => O(m*n)

class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        self.m = len(mat)
        self.n = len(mat[0])

        for i in range(self.m):
            for j in range(self.n):
                if mat[i][j] == 1:

                    mat[i][j] = self.bfs(mat, i, j)

        return mat

    def bfs(self, mat, i, j):
        
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        visited = [[False for _ in range(self.n)] for _ in range(self.m)]
        q = deque()
        q.append([i,j])

        dist = 1

        while q:
            size = len(q)

            for i in range(size):
                curr = q.popleft()

                for dir in dirs:
                    r = curr[0] + dir[0]
                    c = curr[1] + dir[1]

                    if 0 <= r < self.m and 0 <= c < self.n:
                        if mat[r][c] == 0:
                            return dist
                        elif not visited[r][c]:
                            q.append([r,c])
                            visited[r][c] = True

            dist += 1

        return -1
    

# BFS Solution. Process all the 0's together and push them into a queue. Later process the neighbors of 0 and update distance.
# then neighbors of 1 and so on.
# TC: O(m*n)
# SC: O(m*n)

class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        m = len(mat)
        n = len(mat[0])
        q = deque()

        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append([i,j])
                else:
                    mat[i][j] = -1

        dist = 1

        while q:
            size = len(q)

            for k in range(size):
                curr = q.popleft()
                for dir in dirs:
                    r = curr[0] + dir[0]
                    c = curr[1] + dir[1]

                    if 0 <= r < m and 0 <= c < n and mat[r][c] == -1:
                            q.append([r, c])
                            mat[r][c] = dist
            dist += 1

        return mat

# Same as above, but updating mat[r][c] using the curr element (popped element for that loop)
class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        m = len(mat)
        n = len(mat[0])
        q = deque()

        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append([i,j])
                else:
                    mat[i][j] = -1

        while q:
            curr = q.popleft()
            for dir in dirs:
                r = curr[0] + dir[0]
                c = curr[1] + dir[1]

                if 0 <= r < m and 0 <= c < n and mat[r][c] == -1:
                    q.append([r, c])
                    mat[r][c] = mat[curr[0]][curr[1]] + 1

        return mat