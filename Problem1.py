# https://leetcode.com/problems/flood-fill/

# BFS solution with queue
# TC : O(m*n)
# SC: O(m*n)

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q = deque()
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        m = len(image)
        n = len(image[0])
        q.append([sr,sc])

        startColor = image[sr][sc]
        image[sr][sc] = color

        if startColor == color: return image

        while q:

            curr = q.popleft()

            for dir in dirs:
                r = curr[0] + dir[0]
                c = curr[1] + dir[1]

                if 0 <= r < m and 0 <= c < n and image[r][c] == startColor:
                    image[r][c] = color
                    q.append([r,c])

        return image
    
# DFS solution
# TC : O(m*n)
# SC: O(m*n)

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        self.m = len(image)
        self.n = len(image[0])

        startColor = image[sr][sc]

        if startColor == color: return image

        self.dfs(image, sr, sc, startColor, color)
                   
        return image

    def dfs(self, image, i, j, startColor, color):
        
        image[i][j] = color
        for dir in self.dirs:
            r = i + dir[0]
            c = j + dir[1]

            if 0 <= r < self.m and 0 <= c < self.n and image[r][c] == startColor:
                self.dfs(image, r, c, startColor, color)