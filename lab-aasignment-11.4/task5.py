class Graph:
    def __init__(self):
        # The adjacency list maps each node to a list of its neighbors
        self.adj = {}

    def add_edge(self, u, v):
        # Add an edge from u to v (undirected by default)
        if u not in self.adj:
            self.adj[u] = []
        if v not in self.adj:
            self.adj[v] = []
        self.adj[u].append(v)
        self.adj[v].append(u)

    def bfs(self, start):
        """Breadth-First Search traversal from the starting node."""
        from collections import deque
        visited = set()          # Keep track of visited nodes
        queue = deque([start])   # BFS uses a queue
        order = []               # To record traversal order

        while queue:
            node = queue.popleft()
            if node not in visited:
                # Visit node
                visited.add(node)
                order.append(node)
                # Add all unvisited neighbors to the queue
                for neighbor in self.adj.get(node, []):
                    if neighbor not in visited:
                        queue.append(neighbor)
        return order

    def dfs_recursive(self, start):
        """Depth-First Search (recursive implementation)."""
        visited = set()
        order = []

        def dfs(node):
            if node not in visited:
                # Visit node
                visited.add(node)
                order.append(node)
                # Visit each unvisited neighbor recursively
                for neighbor in self.adj.get(node, []):
                    dfs(neighbor)
        dfs(start)
        return order

    def dfs_iterative(self, start):
        """Depth-First Search (iterative implementation using a stack)."""
        visited = set()
        stack = [start]
        order = []

        while stack:
            node = stack.pop()
            if node not in visited:
                # Visit node
                visited.add(node)
                order.append(node)
                # Add unvisited neighbors to the stack (LIFO)
                for neighbor in reversed(self.adj.get(node, [])):  # Reverse for same order as recursive
                    if neighbor not in visited:
                        stack.append(neighbor)
        return order

if __name__ == "__main__":
    graph = Graph()
    print("Create your undirected graph:")
    print("Enter edges as 'u v' (no quotes). Type 'done' to finish.")

    while True:
        line = input("Edge (u v) or 'done': ").strip()
        if line == "done":
            break
        try:
            u, v = line.split()
            graph.add_edge(u, v)
        except ValueError:
            print("Invalid input. Enter two node values separated by a space.")

    if not graph.adj:
        print("Graph is empty.")
    else:
        print("\nAdjacency List:")
        for node in graph.adj:
            print(f"{node}: {graph.adj[node]}")

        while True:
            print("\nCommands: bfs <start>, dfsr <start> (recursive), dfsi <start> (iterative), quit")
            cmd = input("Enter command: ").strip()
            if cmd == "quit":
                break
            elif cmd.startswith("bfs "):
                _, start = cmd.split(maxsplit=1)
                if start not in graph.adj:
                    print(f"Start node '{start}' not in graph.")
                    continue
                order = graph.bfs(start)
                print("BFS traversal order:", order)
            elif cmd.startswith("dfsr "):
                _, start = cmd.split(maxsplit=1)
                if start not in graph.adj:
                    print(f"Start node '{start}' not in graph.")
                    continue
                order = graph.dfs_recursive(start)
                print("DFS (recursive) traversal order:", order)
            elif cmd.startswith("dfsi "):
                _, start = cmd.split(maxsplit=1)
                if start not in graph.adj:
                    print(f"Start node '{start}' not in graph.")
                    continue
                order = graph.dfs_iterative(start)
                print("DFS (iterative) traversal order:", order)
            else:
                print("Unknown command. Try: bfs <start>, dfsr <start>, dfsi <start>, quit")

    # Discussion on DFS:
    print("""
AI DFS Comparison:
------------------
- Recursive DFS is elegant and concise, leveraging the call stack, but may hit recursion limits on deep graphs.
- Iterative DFS uses an explicit stack, avoids recursion limit issues, and can be more efficient for very deep or large graphs.
- Both methods traverse nodes in depth-first order; stack order can affect early/late visit of neighbors.
    """)

