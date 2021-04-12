import collections as c


def BF(graph, starting_node):
    """graph traversal on width is called Breadth First"""
    visited = set([starting_node])  # here there will be added nodes as they are visited.
    coada = c.deque([starting_node])

    while coada:  # as long as we have nodes in the coada
        node = coada.popleft()()  # remove the front node
        print(node, end='')  # print the node
        for i in graph[node]:
            if i not in visited:
                visited.add(i)
                coada.append(i)


def DF(graph, starting_node, visited=None):
    """graph traversal on width is called Depth First"""
    if visited is None:
        visited = set()
    visited.add(starting_node)
    print(starting_node, end='')
    for i in graph[starting_node]:
        if i not in visited:
            DF(graph, i, visited)