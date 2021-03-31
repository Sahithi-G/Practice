    def bfsOfGraph(self, V, adj):
        # code here
        vis=[]
        result=[]
        queue=[]
        queue.append(0)
        while len(queue)>0:
            if queue[0] not in vis:
                queue.extend(adj[queue[0]])
                result.append(queue[0])
                vis.append(queue[0])
            del(queue[0])
        return result
