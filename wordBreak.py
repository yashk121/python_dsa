def wordBreak( s: str, wordDict) -> bool:
    dic = {}
    for i in wordDict:
        dic[i] = 1
    temp = ''

    for i in range(len(s)):
        temp = temp + s[i]
        if temp in dic:
            temp = ''

    if temp in dic or temp == '':
        return True
    return False


def wordBreak(s, dictionary):
    # create a dp table to store results of subproblems
    # value of dp[i] will be true if string s can be segmented
    # into dictionary words from 0 to i.
    dp = [False for i in range(len(s) + 1)]

    # dp[0] is true because an empty string can always be segmented.
    dp[0] = True

    for i in range(len(s) + 1):
        for j in range(i):
            if dp[j] and s[j: i] in dictionary:
                dp[i] = True
                break

    return dp[len(s)]




# This code is contributed by shinjanpatra


if __name__ == '__main__':
    # s = 'aaaaaaa'
    # words = ['aaa','aaaa']
    # print(wordBreak(s,words))
    # driver code
    dictionary = ["mobile", "samsung", "sam", "sung", "man", "mango", "icecream", "and", "go", "i", "like", "ice",
                  "cream"]

    dict = set()
    for s in dictionary:
        dict.add(s)

    if (wordBreak("ilikesamsung", dict)):
        print("Yes")
    else:
        print("No")

    if (wordBreak("iiiiiiii", dict)):
        print("Yes")
    else:
        print("No")

    if (wordBreak("", dict)):
        print("Yes")
    else:
        print("No")

    if (wordBreak("samsungandmango", dict)):
        print("Yes")
    else:
        print("No")

    if (wordBreak("ilikesamsung", dict)):
        print("Yes")
    else:
        print("No")

    if (wordBreak("samsungandmangok", dict)):
        print("Yes")
    else:
        print("No")

