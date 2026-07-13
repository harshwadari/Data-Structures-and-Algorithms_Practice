#733 Flood fill grap using dfs approach

#TC = I(R * C) where r is rows and c is cols and SC = O(R * C) recusion stack space 

def floodFill(image, sr, sc, color):
       
    def dfs(i , j, image,initial_color  , rows,cols,new_color):
        if i < 0 or j < 0 or i >= rows or j >= cols:
            return 
        if image[i][j] != initial_color:
            return 
        if image[i][j] == new_color:
            return 
        image[i][j] = new_color
        dfs(i + 1,j,image,initial_color, rows,cols,new_color)
        dfs(i,j -1,image,initial_color, rows,cols,new_color)
        dfs(i - 1,j,image,initial_color, rows,cols,new_color)
        dfs(i , j + 1,image,initial_color, rows,cols,new_color)
    if image[sr][sc] == color:
        return image
    rows = len(image)
    cols = len(image[0])
    initial_color = image[sr][sc]
    dfs(sr,sc,image,initial_color,rows,cols,color)
    return image


# BFS Approach 
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        if image[sr][sc] == color:
            return image
        queue = deque()
        rows = len(image)
        cols = len(image[0])
        initialcolor = image[sr][sc]
        queue.append((sr,sc))
        while len(queue) != 0:
            i,j = queue.popleft()
            image[i][j] = color
            directions = [(1,0),(0,1),(-1,0),(0,-1)]
            for dx ,dy in directions:
                newI = i + dx
                newJ = j + dy
                if newI < 0 or newI >= rows or newJ < 0 or newJ >= cols:
                    continue
                if image[newI][newJ] != initialcolor:
                    continue
                queue.append((newI,newJ))
        return image