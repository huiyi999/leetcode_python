# https://stackoverflow.com/questions/63999102/balanced-system-files-partition-coding-challenge


def mostBalancedPartition(parent, files_size):
    # Write your code here
    def helper(node, adj, files_size):
        queue = [node]
        weight = 0
        while queue:
            index = queue.pop()
            weight += files_size[index]
            if index in adj:
                queue.extend(adj[index])
        return weight

    adj = {}
    edges = []
    for index, p in enumerate(parent):
        edges.append((p, index))
        if p in adj:
            adj[p].append(index)
        else:
            adj[p] = [index]

    print(adj, edges)
    total_weight = sum(files_size);
    min_diff = sum(files_size);
    for e in edges:
        p, c = e
        adj[p].remove(c)
        w1 = helper(c, adj, files_size)
        min_diff = min(min_diff, abs(total_weight - 2 * w1))
        adj[p].append(c)

    return min_diff
