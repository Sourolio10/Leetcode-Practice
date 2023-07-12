def letterCombinations(digits):
        res = []
        digitToChar = { "2": "abc",
                        "3": "def",
                        "4": "ghi",
                        "5": "jkl",
                        "6": "mno",
                        "7": "qprs",
                        "8": "tuv",
                        "9": "wxyz"}

        def backtrack(i,cur):
            if len(cur) == len(digits):
                res.append(cur)
                return

            for j in digitToChar[digits[i]]:
                backtrack(i+1,cur+j)

        if digits:
            backtrack(0,"")

        return res

if __name__ == "__main__":
    
    n= input()
    x = letterCombinations(n)
    print(*x)