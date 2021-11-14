class TreeNode:
    def __init__(self, data=0, too_big=None, big=None, small=None):
        self.data = data
        self.too_big = too_big
        self.big = big
        self.small = small

class Tree:
    def __init__(self, root=None):
        self.root = root
    
    def insert(self, data):
        if self.root == None:
            self.root = TreeNode(data)
            return
        cur_node = self.root
        while True:
            cur_data = cur_node.data
            diff = data - cur_data
            if diff >= 10:
                if cur_node.too_big == None:
                    cur_node.too_big = TreeNode(data)
                    break
                cur_node = cur_node.too_big
            elif 0 <= diff < 10:
                if cur_node.big == None:
                    cur_node.big = TreeNode(data)
                    break
                cur_node = cur_node.big
            else:
                if cur_node.small == None:
                    cur_node.small = TreeNode(data)
                    break
                cur_node = cur_node.small
                
    def delete(self, data):
        if self.root == None:
            return
    
    def traversal(self):
        self.traversal_tree(self.root)
        
    def traversal_tree(self, cur_node):
        if cur_node == None:
            return
        
        self.traversal_tree(cur_node.small)
        print(cur_node.data)
        self.traversal_tree(cur_node.big)
        self.traversal_tree(cur_node.too_big)


root = Tree()
root.insert(20)
root.insert(40)
root.insert(45)
root.insert(32)

print("Tree contents after insertion using the traversal():")
root.traversal()