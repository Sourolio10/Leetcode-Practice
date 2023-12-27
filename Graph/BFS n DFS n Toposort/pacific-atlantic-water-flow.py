from collections import deque
class Solution:
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        we are suppose to find all the cells from which water can flow to both pacific and 
        atlantic ocean, instead of doing exhaustive dfs search from all the cells and 
        checking if water flows in both oceans, we can start reverse and perform bfs 
        from cells that touch atlantic and pecific oceans and maintain set for both oceans 
        cells, intersecting cells are the ones from whoch water
        will reach both the oceans
        
        '''
        rowlen = len(heights)
        collen = len(heights[0])
        pacific = set({})
        atlantic = set({})
        
        def bfs(queue, s):
            while queue:
                ce = queue.popleft()
                if ce == 'N':
                    if len(queue) == 0:
                        pass
                    else:
                        queue.append('N')
                else:
                    # check if all the elements fall in the category
                    x = [(-1,0),(0,1),(1,0),(0,-1)]
                    for i in x:
                        nr = ce[0] + i[0]
                        nc = ce[1] + i[1]
                        if nr >= 0 and nr < rowlen and nc >= 0 and nc < collen and (nr,nc) not in s and heights[nr][nc] >= heights[ce[0]][ce[1]]:
                            s.add((nr,nc))
                            queue.append((nr,nc))              
            return s
        
        
        q1 = deque()  
        
        # pacific
        for i in range(0,collen):
            if (0,i) not in pacific:
                
                pacific.add((0,i))
                q1.append((0,i))
                
        for i in range(0,rowlen):
            if (i,0) not in pacific:
                pacific.add((i,0))
                q1.append((i,0))
        x = bfs(q1, pacific)
        print(x)
                
        
        
        # atlantic
        q2 = deque()
        for i in range(0,collen):
            if (rowlen-1, i) not in atlantic:
                
                atlantic.add((rowlen-1, i))
                q2.append((rowlen-1, i))
        
        for i in range(0,rowlen):
            if (i,collen-1) not in atlantic:
                
                atlantic.add((i,collen-1))
                q2.append((i,collen-1))
        y = bfs(q2, atlantic)
        print(y)
        return list(x.intersection(y))
        
