# Proszę zaimplementować następujące operacje na drzewie BST 

# 1. wstawianie do drzewa BST
#2. następnik/poprzednik 
#3. Znalezienie minimum/maksimum 

class Node: 
    def __init__(self,val):
        self.right = None 
        self.left - None 
        self.val = val 
    
    def insert(head,item): 
        while True: 
            if head.val >= item: 
                if head.left is None: 
                    head.left = Node(item)
                    return 
                head = head.left
            else: 
                if head.right is None: 
                    head.right = Node(item)
                    return 
                head = head.right
    def next(head,val): 

        node = find(head,val)
        if node.right is None: 
            return None 
        result = node.right 
        while result.left: 
            result = result.left 
        
        return result.val 

        