from collections import deque
def word_ladder(start_word, target_word, word_arr):
    st = set()
    for x in word_arr:
        st.add(x)
    
    q = deque()
    q.append((start_word,1))
    ch = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    while q:
        x = q.popleft()
        word = x[0]
        steps = x[1]

        if word == target_word:
            return steps
        
        for i in range(len(word)):
            for c in ch:
                w = word
                w = w[:i] + c + w[i+1:]

                if w in st:
                    st.remove(w)
                    q.append((w, steps+1))
    
    return 0
                
# Driver Code
if __name__ == "__main__":
    eord_arr=[]
    start_word = input()
    target_word = input()
    word_arr = [(item) for item in input().split(',')]
    print(word_ladder(start_word, target_word, word_arr))