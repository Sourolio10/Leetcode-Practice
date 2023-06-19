def sort(x,n):
    d={}
    for i in x:
        if i in d.keys():
            d[i]+=1
        else:
            d[i]=1
    sorted_tuples = sorted(d.items(), key=lambda x: x[1], reverse=True)
    sorted_dict = dict(sorted_tuples)
    s=""
    for i in sorted_dict.keys():
        s+=i
    return s


#Driver Code
if __name__ == "__main__":
    x = input()
    n = len(x)
    print(sort(x,n))