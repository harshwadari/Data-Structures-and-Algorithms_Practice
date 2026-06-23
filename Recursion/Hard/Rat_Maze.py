class Solution:
    def backtrack(self,i,j,a,n,ans,move,visited):
        if i == n -1 and j == n - 1:
            ans.append(move)
            return
         # downward
        if i + 1 < n and not visited[i + 1][j] and a[i + 1][j] == 1:
            visited[i][j] = 1
            self.backtrack(i + 1,j , a, n, ans, move + 'D', visited)
            visited[i][j] = 0
        # left
        if j - 1 >= 0 and not visited[i][j - 1] and a[i][j - 1] == 1:
            visited[i][j] = 1
            self.backtrack(i,j - 1,a,n,ans,move + 'L',visited)
            visited[i][j] = 0
        # right
        if j + 1 <n and not visited[i][j + 1] and a[i][j + 1] == 1:
            visited[i][j] = 1
            self.backtrack(i,j + 1,a,n,ans,move + 'R',visited)
            visited[i][j] = 0
        # upward
        if i - 1 >= 0 and not visited[i - 1][j] and a[i - 1][j] == 1:
            visited[i][j] = 1
            self.backtrack(i - 1,j , a,n ,ans,move + 'U' , visited)
            visited[i][j] = 0
    def ratInMaze(self, maze):
        # code here
        ans = []
        n = len(maze)
        visited = [[0 for _ in range(n)] for _ in range(n)]
        if maze[0][0] == 1:
            self.backtrack(0,0,maze,n,ans,"",visited)
        return ans
        