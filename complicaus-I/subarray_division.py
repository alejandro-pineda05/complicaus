def birthday(s,d,m):
    if len(s) < m:
        return 0
    else:
        res = 0
        i = 0
        j = m
        while j < len(s):
            arr = s[i:j]
            # print(arr)
            if sum(arr) == d:
                res+=1
            i+=1
            j+=1
        return res
