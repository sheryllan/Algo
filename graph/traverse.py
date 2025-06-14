

def BFS(graph, start, end, path, shortest_path, visited):
    visited.add(start)
    path.append(start)

    if start == end:
        return path

    for node in graph.get(start, []):
        if node not in visited:
            new_path = BFS(graph, node, end, path, shortest_path, visited)
            if new_path:
                shortest_path = new_path

    path.pop()
    return shortest_path


