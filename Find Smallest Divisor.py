def findSmallestDivisor(s, t):
    # Write your code here
    res = 0
    len_s = len(s)
    len_t = len(t)

    if len_s % len_t == 0:
        tmp = t + t
        print(tmp[1:],t)
        index = tmp[1:].find(t)
        print(index)
        if index != -1:
            res = index+1
        else:
            res = -1
    else:
        res = -1
    return res


print(findSmallestDivisor("rbrb", "rbrb"))
