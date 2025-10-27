class QueueList:
    """Queue implementation using Python lists."""
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0


# First, test the list-based queue with user input
print("Queue using list implementation:")
queue_list = QueueList()
while True:
    cmd = input("Enter command (enqueue <value>/dequeue/quit): ").strip()
    if cmd == "quit":
        break
    elif cmd.startswith("enqueue "):
        _, val = cmd.split(maxsplit=1)
        queue_list.enqueue(val)
        print(f"Enqueued: {val}")
    elif cmd == "dequeue":
        try:
            val = queue_list.dequeue()
            print(f"Dequeued: {val}")
        except IndexError as e:
            print("Error:", e)
    else:
        print("Unknown command.")

print("Queue is empty?", queue_list.is_empty())


# === AI Review and Optimized Version ===

"""
AI Queue Performance Review
---------------------------
- The above QueueList uses a Python list and removes elements from the front using pop(0).
- This is inefficient for large queues, because pop(0) has O(n) time complexity (all elements need to be shifted).
- For more efficient queue operations, use collections.deque, which allows O(1) append and popleft operations.
"""

from collections import deque

class QueueDeque:
    """Optimized Queue implementation using collections.deque."""
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.popleft()

    def is_empty(self):
        return not self.items

# Test the optimized deque-based queue with user input
print("\nQueue using deque implementation:")
queue_deque = QueueDeque()
while True:
    cmd = input("Enter command (enqueue <value>/dequeue/quit): ").strip()
    if cmd == "quit":
        break
    elif cmd.startswith("enqueue "):
        _, val = cmd.split(maxsplit=1)
        queue_deque.enqueue(val)
        print(f"Enqueued: {val}")
    elif cmd == "dequeue":
        try:
            val = queue_deque.dequeue()
            print(f"Dequeued: {val}")
        except IndexError as e:
            print("Error:", e)
    else:
        print("Unknown command.")

print("Queue is empty?", queue_deque.is_empty())


"""
Performance Comparison Summary
------------------------------
- QueueList (list-based): enqueue is O(1), but dequeue (pop from start) is O(n).
- QueueDeque (deque-based): both enqueue (append) and dequeue (popleft) are O(1).
- For applications needing lots of queue operations, `collections.deque` should be preferred for efficiency.
"""
