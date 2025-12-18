from collections import deque
from heapq import heappush, heappop
from typing import Dict, List, Union, Optional


def shortest_path(graph: Union[Dict, List], start, end, weighted: bool = False) -> Optional[List]:
    """
    Find the shortest path between start and end nodes.
    
    Args:
        graph: Dict or list representing adjacency list
               - Unweighted: {node: [neighbors]} or [[neighbors]]
               - Weighted: {node: {neighbor: weight}} or list of dicts
        start: Starting node
        end: Target node
        weighted: Boolean indicating if graph is weighted
    
    Returns:
        List of nodes representing the path, or None if no path exists
    """
    # Edge case: start == end
    if start == end:
        return [start]
    
    # Edge case: invalid start or end nodes
    if isinstance(graph, dict):
        if start not in graph or end not in graph:
            return None
    elif isinstance(graph, list):
        max_node = len(graph) - 1
        if start < 0 or start > max_node or end < 0 or end > max_node:
            return None
    
    if weighted:
        return _dijkstra_shortest_path(graph, start, end)
    else:
        return _bfs_shortest_path(graph, start, end)


def _bfs_shortest_path(graph: Union[Dict, List], start, end) -> Optional[List]:
    """
    Find shortest path using BFS for unweighted graphs.
    """
    queue = deque([start])
    visited = {start}
    parent = {start: None}
    
    while queue:
        current = queue.popleft()
        
        # Get neighbors based on graph representation
        if isinstance(graph, dict):
            neighbors = graph.get(current, [])
        else:
            neighbors = graph[current] if current < len(graph) else []
        
        for neighbor in neighbors:
            if neighbor == end:
                # Reconstruct path
                path = [end]
                node = current
                while node is not None:
                    path.append(node)
                    node = parent[node]
                return path[::-1]
            
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)
    
    return None  # No path exists


def _dijkstra_shortest_path(graph: Union[Dict, List], start, end) -> Optional[List]:
    """
    Find shortest path using Dijkstra's algorithm for weighted graphs.
    """
    # Initialize distances and parent tracking
    distances = {}
    parent = {}
    visited = set()
    
    # Priority queue: (distance, node)
    pq = [(0, start)]
    distances[start] = 0
    parent[start] = None
    
    while pq:
        current_dist, current = heappop(pq)
        
        # Skip if already processed with a shorter distance
        if current in visited:
            continue
        
        visited.add(current)
        
        # Early termination if we reached the end
        if current == end:
            # Reconstruct path
            path = []
            node = end
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1]
        
        # Get neighbors and weights based on graph representation
        if isinstance(graph, dict):
            neighbors = graph.get(current, {})
            if isinstance(neighbors, dict):
                # Weighted: {neighbor: weight}
                for neighbor, weight in neighbors.items():
                    new_dist = current_dist + weight
                    if neighbor not in distances or new_dist < distances[neighbor]:
                        distances[neighbor] = new_dist
                        parent[neighbor] = current
                        heappush(pq, (new_dist, neighbor))
            else:
                # Unweighted but in dict format: [neighbors] with weight 1
                for neighbor in neighbors:
                    new_dist = current_dist + 1
                    if neighbor not in distances or new_dist < distances[neighbor]:
                        distances[neighbor] = new_dist
                        parent[neighbor] = current
                        heappush(pq, (new_dist, neighbor))
        else:
            # List representation
            if current < len(graph):
                neighbors = graph[current]
                if isinstance(neighbors, dict):
                    # Weighted: list of dicts
                    for neighbor, weight in neighbors.items():
                        new_dist = current_dist + weight
                        if neighbor not in distances or new_dist < distances[neighbor]:
                            distances[neighbor] = new_dist
                            parent[neighbor] = current
                            heappush(pq, (new_dist, neighbor))
                else:
                    # Unweighted: list of lists with weight 1
                    for neighbor in neighbors:
                        new_dist = current_dist + 1
                        if neighbor not in distances or new_dist < distances[neighbor]:
                            distances[neighbor] = new_dist
                            parent[neighbor] = current
                            heappush(pq, (new_dist, neighbor))
    
    return None  # No path exists


# Test cases
if __name__ == "__main__":
    # Test 1: Unweighted directed graph (dict representation)
    print("Test 1: Unweighted directed graph (dict)")
    graph1 = {
        0: [1, 2],
        1: [3],
        2: [3],
        3: [4],
        4: []
    }
    result1 = shortest_path(graph1, 0, 4, weighted=False)
    print(f"Path from 0 to 4: {result1}")  # Expected: [0, 1, 3, 4] or [0, 2, 3, 4]
    assert result1 is not None
    assert result1[0] == 0 and result1[-1] == 4
    
    # Test 2: Unweighted directed graph (list representation)
    print("\nTest 2: Unweighted directed graph (list)")
    graph2 = [
        [1, 2],  # node 0
        [3],     # node 1
        [3],     # node 2
        [4],     # node 3
        []       # node 4
    ]
    result2 = shortest_path(graph2, 0, 4, weighted=False)
    print(f"Path from 0 to 4: {result2}")  # Expected: [0, 1, 3, 4] or [0, 2, 3, 4]
    assert result2 is not None
    assert result2[0] == 0 and result2[-1] == 4
    
    # Test 3: Weighted directed graph (dict representation)
    print("\nTest 3: Weighted directed graph (dict)")
    graph3 = {
        0: {1: 4, 2: 1},
        1: {3: 1},
        2: {1: 2, 3: 5},
        3: {4: 3},
        4: {}
    }
    result3 = shortest_path(graph3, 0, 4, weighted=True)
    print(f"Path from 0 to 4: {result3}")  # Expected: [0, 2, 1, 3, 4] (cost: 1+2+1+3=7)
    assert result3 is not None
    assert result3[0] == 0 and result3[-1] == 4
    
    # Test 4: No path exists
    print("\nTest 4: No path exists")
    graph4 = {
        0: [1],
        1: [2],
        2: [],
        3: [4],
        4: []
    }
    result4 = shortest_path(graph4, 0, 4, weighted=False)
    print(f"Path from 0 to 4: {result4}")  # Expected: None
    assert result4 is None
    
    # Test 5: Start == end
    print("\nTest 5: Start == end")
    result5 = shortest_path(graph1, 2, 2, weighted=False)
    print(f"Path from 2 to 2: {result5}")  # Expected: [2]
    assert result5 == [2]
    
    # Test 6: Invalid nodes
    print("\nTest 6: Invalid nodes")
    result6 = shortest_path(graph1, 0, 10, weighted=False)
    print(f"Path from 0 to 10: {result6}")  # Expected: None
    assert result6 is None
    
    print("\nAll tests passed!")

