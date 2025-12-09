class TreeNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key, value=None):
        if not self.root:
            self.root = TreeNode(key, value)
            return
        
        node = self.root
        while True:
            if key < node.key:
                if not node.left:
                    node.left = TreeNode(key, value)
                    break
                node = node.left
            elif key > node.key:
                if not node.right:
                    node.right = TreeNode(key, value)
                    break
                node = node.right
            else:
                node.value = value
                break
    
    def search(self, key):
        node = self.root
        while node:
            if key == node.key:
                return node.value
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return None
    
    def delete(self, key):
        def find_min(root):
            while root.left:
                root = root.left
            return root
        
        def delete_node(root, key):
            if not root:
                return root
            
            if key < root.key:
                root.left = delete_node(root.left, key)
            elif key > root.key:
                root.right = delete_node(root.right, key)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                
                temp = find_min(root.right)
                root.key = temp.key
                root.value = temp.value
                root.right = delete_node(root.right, temp.key)
            
            return root
        
        self.root = delete_node(self.root, key)
    
    def height(self):
        def get_height(node):
            if not node:
                return 0
            left_h = get_height(node.left)
            right_h = get_height(node.right)
            return max(left_h, right_h) + 1
        
        return get_height(self.root)
    
    def is_balanced(self):
        def check(node):
            if not node:
                return 0
            
            left = check(node.left)
            if left == -1:
                return -1
            
            right = check(node.right)
            if right == -1:
                return -1
            
            if abs(left - right) > 1:
                return -1
            
            return max(left, right) + 1
        
        return check(self.root) != -1
    