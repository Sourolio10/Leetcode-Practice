
def subsec_abc(n):
    c= l =0
    dic = {x:0 for x in "abc"}

    for r in range(len(n)):
        dic[n[r]]+=1

        while dic["a"] and dic["b"] and dic["c"]:
            dic[n[l]]-=1
            l+=1
        c+=l
    return c

if __name__ == "__main__":
    
    n= input()
    print(subsec_abc(n))