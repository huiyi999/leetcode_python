'''
A tree is an undirected graph in which any two vertices are connected by exactly one path.
In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges
where edges[i] = [ai, bi] indicates that there is an undirected edge
between the two nodes ai and bi in the tree, you can choose any node of the tree as the root.
When you select a node x as the root, the result tree has height h. Among all possible rooted trees,
those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.


Constraints:
1 <= n <= 2 * 104
edges.length == n - 1
0 <= ai, bi < n
ai != bi
All the pairs (ai, bi) are distinct.
The given input is guaranteed to be a tree and there will be no repeated edges.

'''

'''
首先证明这个根的数量最多为2.

证明：假设符合条件的根可以有3个，3个树根的高度都是H,可以知道，为了达到最小高度，符合条件的根尽可能在一起。
但是与三个高度都是H相悖。应有两个h，一个h+1。由此也可以证4,5....个的情况。
那么2个为什么可以存在呢，考虑一个完全对称（其实也不用考虑对称图，示例的图就符合两个根了）的图，中心的两个根就是解。

这样我们采取修剪的办法。
每一轮修剪一次所有叶子节点，一旦节点数量只有1或者2，停止修剪，返回答案。

在python里用集合弹出节点更快（平均情况下，list插入删除都是n时间，set是1时间。
'''
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [set() for x in range(n)]

        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])
        nodes = set([x for x in range(n)])

        while len(nodes) > 2:
            removed = []
            for u in range(n):
                if len(graph[u]) == 1:
                    removed.append(u)
            for u in removed:
                v = graph[u].pop()
                graph[v].remove(u)
                nodes.remove(u)
        return list(nodes)

'''
Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.

Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]

Input: n = 1, edges = []
Output: [0]

Input: n = 2, edges = [[0,1]]
Output: [0,1]

'''
