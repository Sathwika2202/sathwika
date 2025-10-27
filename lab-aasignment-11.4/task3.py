class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Points to the next node in the list (or None if last)

class LinkedList:
    def __init__(self):
        self.head = None  # Start of the linked list

    def insert_at_end(self, data):
        """Inserts a node with the given data at the end of the list."""
        new_node = Node(data)
        if self.head is None:
            # The list is empty; new node becomes the head.
            self.head = new_node
            # AI: head pointer is updated to point to the new node.
        else:
            current = self.head
            while current.next:
                current = current.next
            # current is now the last node. Link its 'next' pointer to new_node.
            current.next = new_node
            # AI: The last node's next pointer is updated to reference the new node.

    def delete_value(self, target):
        """Deletes the first node with the specified value."""
        current = self.head
        prev = None
        while current:
            if current.data == target:
                if prev is None:
                    # Deleting the head node
                    self.head = current.next
                    # AI: head pointer is updated to skip the removed node.
                else:
                    # Remove node by updating previous node's next pointer
                    prev.next = current.next
                    # AI: prev's next pointer now skips 'current' and points to 'current.next'.
                print(f"Deleted node with value: {target}")
                return
            prev = current
            current = current.next
        print(f"Value {target} not found in the list.")

    def traverse(self):
        """Prints all elements in the list."""
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print("Linked List:", " -> ".join(elements) if elements else "(empty)")

# ==== Console Interaction ====
if __name__ == "__main__":
    ll = LinkedList()
    print("Singly Linked List Operations:")
    print("Commands: insert <value>, delete <value>, traverse, quit")
    while True:
        cmd = input("Enter command: ").strip()
        if cmd == "quit":
            break
        elif cmd.startswith("insert "):
            _, val = cmd.split(maxsplit=1)
            ll.insert_at_end(val)
            print(f"Inserted: {val}")
        elif cmd.startswith("delete "):
            _, val = cmd.split(maxsplit=1)
            ll.delete_value(val)
        elif cmd == "traverse":
            ll.traverse()
        else:
            print("Unknown command. Try: insert <v>, delete <v>, traverse, quit")

"""
AI Suggested Test Cases:
-----------------------
1. Insert into an empty list (then traverse).
2. Insert multiple nodes (traverse to confirm order).
3. Delete the head node (when list has multiple elements).
4. Delete the only node (should result in empty list).
5. Delete a node that does not exist (should print not found).
6. Delete a middle node and traverse (check linkage).
7. Delete last node and traverse.
8. Mix insertions and deletions, traversing between them.
9. Traverse empty list.
"""
