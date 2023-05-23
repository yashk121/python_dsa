def isSafe(i, j, m, n):
    return (0 <= i and i < m and 0 <= j and j < n)


def func(i, j, grid, m, n, index, str, ans):
    if (i >= m or j >= n or index >= len(str)):
        return

    if (isSafe(i, j, m, n)):
        if (grid[i][j] == str[index]):
            ans.append((i, j))
            if (index == len(str) - 1):
                print(ans)
                ans.remove((i,j))
                return

            func(i + 1, j, grid, m, n, index + 1, str, ans)
            func(i, j + 1, grid, m, n, index + 1, str, ans)
            ans.remove((i, j))


if __name__ == '__main__':
    grid = [
        ['c', 'c', 't', 'n', 'a', 'x'],
        ['c', 'c', 'a', 't', 'n', 't'],
        ['a', 'c', 'n', 'n', 't', 't'],
        ['t', 'n', 'i', 'i', 'p', 'p'],
        ['a', 'o', 'o', 'o', 'a', 'a'],
        ['s', 'a', 'a', 'a', 'o', 'o'],
        ['k', 'a', 'i', 'o', 'k', 'i'],
    ]
    ans = []
    m = len(grid)
    n = len(grid[0])
    for i in range(0, m):
        for j in range(0, n):
            func(i, j, grid, 7, 6, 0, 'cat', ans)
