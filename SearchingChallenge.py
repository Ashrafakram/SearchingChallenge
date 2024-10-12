def SearchingChallenge(strArr):
    # Convert the input to a 2D matrix of integers
    matrix = [list(map(int, row)) for row in strArr]
    rows, cols = len(matrix), len(matrix[0])
    
    # Helper function to perform DFS and mark connected 0's as visited
    def dfs(i, j):
        # Check if we are out of bounds or the cell is not 0
        if i < 0 or i >= rows or j < 0 or j >= cols or matrix[i][j] != 0:
            return
        # Mark the current cell as visited (change 0 to 1)
        matrix[i][j] = 1
        # Explore the four directions: up, down, left, right
        dfs(i - 1, j)  # Up
        dfs(i + 1, j)  # Down
        dfs(i, j - 1)  # Left
        dfs(i, j + 1)  # Right

    # Variable to count the number of holes
    hole_count = 0

    # Loop through every cell in the matrix
    for i in range(rows):
        for j in range(cols):
            # If we find a 0, it's a new hole
            if matrix[i][j] == 0:
                # Start DFS from this 0 and mark all connected 0's
                dfs(i, j)
                # Increment the hole count after finishing the DFS
                hole_count += 1

    return hole_count

# keep this function call here
print(SearchingChallenge(input()))
