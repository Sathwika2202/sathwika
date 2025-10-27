class Node:
    """
    Node for Binary Search Tree.

    Attributes:
        data (int): Value of the node.
        left (Node): Left child node.
        right (Node): Right child node.
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    """
    Binary Search Tree implementation with insert, search, and in-order traversal.

    Methods:
        insert(value): Inserts value into BST.
        search(value): Returns True if value is present, False otherwise.
        inorder_traversal(): Returns a list of node values in order.
    """
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert value into BST."""
        def _insert(node, value):
            if node is None:
                return Node(value)
            if value < node.data:
                node.left = _insert(node.left, value)
            elif value > node.data:
                node.right = _insert(node.right, value)
            # If value == node.data, do not insert duplicate
            return node
        self.root = _insert(self.root, value)

    def search(self, value):
        """Return True if value is found, False otherwise."""
        def _search(node, value):
            if node is None:
                return False
            if node.data == value:
                return True
            elif value < node.data:
                return _search(node.left, value)
            else:
                return _search(node.right, value)
        return _search(self.root, value)

    def inorder_traversal(self):
        """Return list of BST elements in in-order (sorted order)."""
        result = []
        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.data)
                _inorder(node.right)
        _inorder(self.root)
        return result

if __name__ == "__main__":
    print("Enter integers to insert into BST (space-separated):")
    nums = input().strip()
    bst = BST()
    if nums:
        for num in nums.split():
            bst.insert(int(num))

    print("\nBST in-order traversal (sorted):")
    print(bst.inorder_traversal())

    while True:
        cmd = input("\nEnter command (search <value>/traverse/quit): ").strip()
        if cmd == "quit":
            break
        elif cmd == "traverse":
            print("BST in-order traversal:", bst.inorder_traversal())
        elif cmd.startswith("search "):
            try:
                _, val = cmd.split(maxsplit=1)
                val = int(val)
                found = bst.search(val)
                if found:
                    print(f"{val} found in BST.")
                else:
                    print(f"{val} not found in BST.")
            except ValueError:
                print("Invalid value for search.")
        else:
            print("Unknown command. Try 'search <value>', 'traverse', or 'quit'.")
