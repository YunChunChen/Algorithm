def spray_check(degree, edge):
    max_node = degree.index(max(degree))
    for node in edge[max_node]:
        if degree[node] != 0:
            degree[node] = degree[node] - 1
    degree[max_node] = 0
    return max_node

if __name__ == '__main__':
    C, R = [int(num) for num in input().split()]
    edge = {}
    for i in range(1, C+1):
        edge[i] = []
    for i in range(R):
        key, val = [int(num) for num in input().split()]
        edge[key].append(val)
        edge[val].append(key)
    degree = [0] * (C+1)
    for key in edge.keys():
        degree[key] = len(edge[key])
    ans = []
    while sum(degree) != 0:
        node = spray_check(degree, edge)
        ans.append(node)
    print(len(ans))
    print(' '.join(str(num) for num in sorted(ans)))
