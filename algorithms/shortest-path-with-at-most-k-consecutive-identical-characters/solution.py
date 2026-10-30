class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        import heapq
        def my_function(n,edges, labels,k):
            tree={i:[] for i in range(len(labels))}
            weight={}
            for u,v,w in edges:
                tree[u].append((v,w))
            q=[]
            heapq.heappush(q,(0,0,1))
            visited={}
            while q:
                cost,node, count=heapq.heappop(q)
                if node==n-1:
                    return cost
                if (node, count) in visited and visited[(node,count)]<=cost:
                    continue
                visited[(node, count)]=cost

                for v,w in tree[node]:
                    
                    new_cost=cost+w
                    next_cost=w+cost
                    if labels[node]==labels[v]:
                        new_count=count+1
                    else:
                        new_count=1
                    
                    if new_count<=k:
                        heapq.heappush(q,(new_cost,v,new_count))


            return -1
        

        return my_function(n,edges, labels,k)




            
            


            

