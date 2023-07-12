def combinationSum2(candidates, target):
    ans = []
    ds = []
    candidates.sort()


    def findCombination(ind: int, target: int):
        if target == 0:
            ans.append(ds[:])
            return
        for i in range(ind, len(candidates)):
            if i > ind and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                break
            ds.append(candidates[i])
            findCombination(i + 1, target - candidates[i])
            ds.pop()


    findCombination(0, target)
    return ans




if __name__ == "__main__":
    arr=[]
    arr = [int(item) for item in input().split(',')]
    n= len(arr)
    s = int(input())
    d =[]
    comb = combinationSum2(arr, s)
    print(*comb)