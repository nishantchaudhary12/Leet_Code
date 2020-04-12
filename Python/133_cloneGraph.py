'''Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def _helper(node):
            if node in visited:
                return visited[node]
            new = Node(node.val)
            visited[node] = new
            if node.neighbors:
                for each in node.neighbors:
                    new.neighbors.append(_helper(each))
            return new

        if not node:
            return node
        visited = dict()
        clone = _helper(node)
        return clone
