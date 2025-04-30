from collections import deque

def tree_by_levels(node):
    if node is None:
        return []
    
    nodes = []
    queue = deque([node])

    while queue:
        curr = queue.popleft()
        nodes.append(curr.value)
        
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    
    return nodes
    
        
