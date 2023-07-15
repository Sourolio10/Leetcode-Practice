
def lru_cache(i,s,word_dict):
    res = False
    if i>=len(s):
        return True
    
    for word in word_dict:
        if s[i: i+ len(word)] == word:
            res = res or lru_cache(i+len(word),s,word_dict)
    return res

if __name__ == "__main__":
    
    s= input()
    word_dict = [(item) for item in input().split(',')]
    print(lru_cache(0,s,word_dict))