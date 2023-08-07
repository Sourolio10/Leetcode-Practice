from queue import PriorityQueue
def min_no_of_steps(start,  end, arr_steps):
    q = PriorityQueue()
    dist = [int(1e9)] * 100000
    
    dist[0] = 0
    
    q.put((start,0))
    mod = 100000
    while not q.empty():
        node, steps = q.get()
        for s in arr_steps:
            num = (s * node) % mod
            if dist[num] > steps + 1:
                dist[num] = steps + 1
                if num == end:
                    return steps + 1
                q.put((num, steps  + 1))
               
    return -1


steps = [2,5,7]
start =3
end = 30
print(min_no_of_steps(start,  end, steps))