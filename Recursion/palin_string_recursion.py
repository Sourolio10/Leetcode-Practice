def Palin(S,start,end):
    if start >= end:
        return True
    elif S[start] == S[end]:
        return Palin(S,start+1,end-1)
    else:
        return False

# Driver Code
if __name__ == "__main__":
    
    S = input()
    n = len(S)
    print(Palin(S,0,n-1))
    