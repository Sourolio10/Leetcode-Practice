def subsec_abc(n, k):
    c= l =0
    d=""
    minl=9999999
    min_s=""
    dic = {x:0 for x in k}

    for r in range(len(n)):
        if n[r] in dic:
            dic[n[r]]+=1

        while all(dic.values()):
            if n[l] in dic:
                dic[n[l]]-=1
            l+=1
        c+=l
        d = n[l:r]
        if len(d) < minl:
            minl = len(d)
            min_s = d
    return min_s

if __name__ == "__main__":
    
    n= input()
    k = input()
    print(subsec_abc(n, k))