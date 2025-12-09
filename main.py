from bst import BinarySearchTree

class BSTDemo:
    def __init__(self):
        self.tree = BinarySearchTree()
        self.demo_keys = [50, 30, 70, 20, 40, 60, 80]
        for key in self.demo_keys:
            self.tree.insert(key, f"val_{key}")
    
    def menu(self):
        print("\n=== BST DEMO ===")
        print("1. INSERT")
        print("2. SEARCH")
        print("3. DELETE")
        print("4. HEIGHT")
        print("5. IS_BALANCED")
        print("6. RESET")
        print("7. EXIT")
    
    def run(self):
        while True:
            self.menu()
            cmd = input("Command: ").strip()
            
            if cmd == "1":
                self.insert_demo()
            elif cmd == "2":
                self.search_demo()
            elif cmd == "3":
                self.delete_demo()
            elif cmd == "4":
                self.height_demo()
            elif cmd == "5":
                self.balance_demo()
            elif cmd == "6":
                self.reset_demo()
            elif cmd == "7":
                break
            else:
                print("Wrong command")
    
    def insert_demo(self):
        print("\n--- INSERT ---")
        try:
            key = int(input("Key: "))
            value = input("Value (Enter for none): ").strip()
            if value:
                self.tree.insert(key, value)
                print(f"Added {key}")
            else:
                self.tree.insert(key)
                print(f"Added {key} without value")
        except:
            print("Error")
    
    def search_demo(self):
        print("\n--- SEARCH ---")
        try:
            key = int(input("Key to search: "))
            result = self.tree.search(key)
            if result is not None:
                print(f"Found: {result}")
            else:
                print("Not found")
        except:
            print("Error")
    
    def delete_demo(self):
        print("\n--- DELETE ---")
        try:
            key = int(input("Key to delete: "))
            self.tree.delete(key)
            print(f"Deleted {key}")
        except:
            print("Error")
    
    def height_demo(self):
        print("\n--- HEIGHT ---")
        h = self.tree.height()
        print(f"Tree height: {h}")
    
    def balance_demo(self):
        print("\n--- IS_BALANCED ---")
        bal = self.tree.is_balanced()
        print(f"Balanced: {bal}")
    
    def reset_demo(self):
        self.tree = BinarySearchTree()
        for key in self.demo_keys:
            self.tree.insert(key, f"val_{key}")
        print("\nTree reset to demo state")

if __name__ == "__main__":
    demo = BSTDemo()
    demo.run()
    