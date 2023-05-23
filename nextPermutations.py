if __name__ == '__main__':
    a = [3, 5, 2, 1, 3, 7, 5, 9, 3]
    b = [2,3,4]
    c = [2,3,4]
    li = []
    li.append(a)
    li.append(b)
    li.append(c)
    d = set()
    d.update(li)

    print(d)
