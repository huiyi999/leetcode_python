'''
Given a reference of a node in a connected undirected graph. Return a deep copy (clone) of the graph.
Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.
class Node {
    public int val;
    public List<Node> neighbors;
}

Test case format:
For simplicity sake, each node's value is the same as the node's index (1-indexed).
For example, the first node with val = 1, the second node with val = 2, and so on.
The graph is represented in the test case using an adjacency list.

Adjacency list is a collection of unordered lists used to represent a finite graph.
Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.
'''
'''
一般的遍历只需要保存是否遍历过这个节点即可，但是由于这个题需要把neighboors对应复制过来。
那么需要进行改进，改进的方式是把set改成dict，保存每个老节点对应的新节点是多少。
在Python中，字典直接保存对象（指针）之间的映射。所以，我们直接把遍历过的对象和复制出来的对象一一对应即可。
当我们遍历到一个新的节点的时候，需要判断这个节点是否在字典中出现过，
如果出现过就把它对应的复制出来的对象放到其neighboors里，
若没有出现过，那么就重新构造该节点，并把原节点和该节点放到字典中保存。
'''


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def __int__(self):
        self.visited = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        """
        make copy of every node
        recursivelly update by passing the node
        """
        if not node: return None
        if node in self.visited:
            return self.visited[node]

        new_node = Node(node.val, [])
        if node.neighbors:
            new_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]
        return new_node

    def cloneGraph1(self, node: 'Node') -> 'Node':
        node_copy = self.dfs(node, dict())
        return node_copy

    def dfs1(self, node, hashd):
        if not node: return None
        if node in hashd: return hashd[node]
        node_copy = Node(node.val, [])
        hashd[node] = node_copy
        for n in node.neighbors:
            n_copy = self.dfs1(n, hashd)
            if n_copy:
                node_copy.neighbors.append(n_copy)
        return node_copy

    def cloneGraph2(self, node: 'Node') -> 'Node':
        if not node: return None

        new_nodes = dict()
        return self.dfs2(node, new_nodes)

    def dfs2(self, node, new_nodes: dict()) -> 'Node':
        # 'node' is always an 'old' node and not its copy (if it exists)
        if node.val in new_nodes:
            # node is already being cloned at upper levels of the recursion
            return new_nodes[node.val]
        # else this is our first encounter with the node
        new_neighbours = []
        new_node = Node(node.val, new_neighbours)
        new_nodes[node.val] = new_node

        for neighbour in node.neighbors:
            # recursively clone neighbour
            new_neighbour = self.dfs(neighbour, new_nodes)
            new_neighbours.append(new_neighbour)

        return new_node


solution = Solution()
node1 = Node(1, [2, 4])


'''
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.

Input: adjList = [[2],[1]]
Output: [[2],[1]]
'''
