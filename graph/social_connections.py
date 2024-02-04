"""
A popular social media platform provides a feature to connect people online.
Connections are represented as an undirected graph where a user can see the profiles of those they are connected to.

There are connection nodes users numbered 1 to connection_nodes, and connection_edges connections where the i-th pair
connects nodes connection_from[i] and connection_to[i].
The queries array contains node numbers.

Find the number of users whose profiles are visible to query[i].
Report an array of integers where the i-th value is the answer to the i-th query.


Example:
    connection_nodes = 7
    connection_edges = 4
    connection_from = [1,2,3,5]
    connection_to = [2,3,4,6]
    queries = [1,3,5,7]

    Graph looks lik
    7
    5--6
    1--2--3--4

    So the visible profiles for the queries:
    query     visible profiles     # visible profiles
    1           [1,2,3,4]           4
    3           [1,2,3,4]           4
    5           [5,6]               2
    7           [7]                 1

    The answer is [4,4,2,1]
"""


class User:
    def __init__(self, n):
        self.n = n
        self.edges = set()

    # def __hash__(self):
    #     return hash(self.n)
    #
    # def __eq__(self, other):
    #     return self.n == other or isinstance(other, User) and self.n == other.n and self.edges == other.edges


# u1 = User(0)
# u2 = User(0)
# u3 = User(1)
#
# d = {u1: 2, u3: 1}
# print(d[0])
#
# ll = [1, 2, 3]
# print(ll[u1])

def get_visible_profile_count(connection_nodes, connection_from, connection_to, queries):
    node_pool = [User(i) for i in range(1, connection_nodes + 1)]
    visited = [False] * connection_nodes
    for i_from, i_to in zip(connection_from, connection_to):
        from_node = node_pool[i_from - 1]
        to_node = node_pool[i_to - 1]
        from_node.edges.add(i_to)
        to_node.edges.add(i_from)

    # traverse the graph
    def traverse(node: User, visited, connections: set):
        visited[node.n - 1] = True
        connections.add(node.n)
        for e in node.edges:
            if not visited[e - 1]:
                traverse(node_pool[e - 1], visited, connections)

    visible_profiles = {}
    for node in node_pool:
        if not visited[node.n - 1]:
            connections = set()
            traverse(node, visited, connections)
            for c in connections:
                visible_profiles[c] = len(connections)

    return [visible_profiles[q] for q in queries]



connection_nodes = 7
connection_from = [1,2,3,5,4,5]
connection_to = [2,3,4,6,1,7]
queries = [1,3,5,7]

result = get_visible_profile_count(connection_nodes, connection_from, connection_to, queries)
print(result)

