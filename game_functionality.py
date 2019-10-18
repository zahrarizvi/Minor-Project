def riversizes(matrix):
    sizes = []
    visited = [[False for value in row]for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j]:
                continue
            treverseNode(i, j, matrix, visited,sizes)
    return sizes
def treverseNode(i,j,matrix,visited,sizes):
    currentriversize = 0
    #using stacks for depth first search
    nodestoexplore = [[i,j]]
    while len(nodestoexplore):
        currentNode = nodestoexplore.pop()
        i = currentNode[0]
        j = currentNode[1]
        if visited[i][j]:
            continue
        visited[i][j] = True
        if matrix[i][j] == 0:
            continue
        currentriversize += 1
        unVisitedNeighbors = getUnvisitedNeighbors(i,j,matrix,visited)
        for neighbour in unVisitedNeighbors:
            nodestoexplore.append(neighbour)
    if currentriversize > 0:
        sizes.append(currentriversize)
def getUnvisitedNeighbors(i,j,matrix,visited):
    unVisitedNeighbors = []
    if i > 0 and not visited[i-1][j]:
        unVisitedNeighbors.append([i-1,j])
    if i < len(matrix) - 1 and not visited[i+1][j]:
        unVisitedNeighbors.append([i+1,j])
    if j > 0 and not visited[i][j-1]:
        unVisitedNeighbors.append([i,j-1])
    if j < len(matrix[0]) -1 and not visited[i][j+1]:
        unVisitedNeighbors.append([i,j+1])
    return unVisitedNeighbors