stays = 0
not_stay = 0
x_move = [2, 1, -2, -1, -2, -1, 2, 1]
y_move = [1, 2, -1, -2, 1, 2, -1, -2]


def isSafe(n, row, col):
    if row >= 0 and col >= 0 and row < n and col < n:
        return True
    return False


def knightUtil(n, k, row, col, count):
    global stays
    if count == k:
        stays += 1
        return

    for i in range(8):
        if isSafe(n, row + x_move[i], col + y_move[i]):
            knightUtil(n, k, row + x_move[i], col + y_move[i], count + 1)
    return


class Solution:

    def knightProbability(self, n: int, k: int, row: int, col: int) -> float:
        board = [[-1 for i in range(n)] for j in range(n)]
        knightUtil(n, k, row, col, 0)
        ans = float((float(stays) ) / 8 ** k)
        return ans


if __name__ == '__main__':
    ob = Solution()
    ans = ob.knightProbability(8, 30, 6, 4)
    print(ans)
