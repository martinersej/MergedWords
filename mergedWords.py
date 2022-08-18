def isMerged(x,y,z):
    x = split(x)
    y = split(y)
    z = split(z)

    return mergedWords(x,y,z)

def mergedWords(x,y,z):
    grid = gridCreator(x,y)

    for i in range(len(x)+1):
        for j in range(len(y)+1):
            grid[i][j] = 1 if M(i,j,x,y,z   ) == True else 0
    
    if grid[len(x)][len(y)] == 1:
        zSubsequenceX(grid, x, y)
        return True
    else:
        return False

def M(i, j, x, y, z):
    if i == 0 and j == 0:
        return True
    elif j > 0 and i == 0:
        return z[j] == y[j] and M(0, j - 1)
    elif j == 0 and i > 0:
        return z[i] == x[i] and M(i - 1, 0)
    elif i > 0 and j > 0:
        return (z[i+j] == y[j] and M(i,j-1)) or (z[i+j] == x[i] and M(i-1,j))
    return False

def zSubsequenceX(grid, x, y):
    indexes = []
    i = len(x)
    j = len(y)
    while i+j > 0:
        if i == 0:
            break
        elif j == 0:
            indexes.append(i-1)
            i = i - 1
        else:
            if grid[i-1][j] == 1:
                indexes.append(j+i-1)
                i = i - 1
            else:
                j = j - 1
    indexes.reverse()
    print(indexes)
