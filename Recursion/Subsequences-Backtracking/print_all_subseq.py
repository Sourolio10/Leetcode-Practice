def subseq(i,s,f):
    if i == len(s):
        print(f+"")
        return
    subseq(i+1,s,f+s[i])

    subseq(i+1,s,f)

if __name__ == "__main__":
    s = input()
    subseq(0,s,'')