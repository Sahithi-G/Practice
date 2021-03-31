    def levelOrder(self,root ):
        # Code here
        queue =[]
        result =[]

        queue.append(root)
        while(len(queue)>0):
            root = queue[0]
            if root:
                queue.append(root.left)
                queue.append(root.right)
                result.append(root.data)
            del(queue[0])
        return result 
