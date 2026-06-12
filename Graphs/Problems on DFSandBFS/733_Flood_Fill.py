#733 Flood fill grap using dfs approach

#TC = I(R * C) where r is rows and c is cols and SC = O(R * C) recusion stack space 

def floodFill(self, image, sr, sc, color):
       
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
