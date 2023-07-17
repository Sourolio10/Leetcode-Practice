
def fruits(s):
    two_types=set()
    max_fruit =0
    for i in s:
        if len(two_types) == 2:
            if i not in two_types:
                break
            else:
                max_fruit+=1
        else:
            two_types.add(i)
            max_fruit+=1
    return max_fruit


if __name__ == "__main__":
    s= input()
    print(fruits(s))