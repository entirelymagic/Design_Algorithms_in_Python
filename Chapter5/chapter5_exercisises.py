from Chapter5 import ordered_graphs as og

g1 = {
    1: [2, 3, 5],
    2: [3],
    3: [4],
    4: [1],
    5: [3, 4, 6],
    6: [1, 3],
    7: [],
    8: [],
}

g2 = {  # figure 5.1
    1: [2, 3],
    2: [3],
    3: [6],
    4: [3],
    5: [4],
    6: [5],
    7: [8],
    8: [],
}

g3 = {
    1: [2, 3],
    2: [1, 3],
    3: [6],
    4: [3],
    5: [4],
    6: [5],
    7: [8],
    8: [],
}

# for i in (g1, g2, g3):
#     print('Graph : ', i)
#     print('Isolated nodes', og.isolateDiGraph(i))
#     print('path: ', og.path(i, 1, 4))
#     print('all path: ', og.all_paths(i, 1, 4))
#     print('shortest path', og.shortest_path(i, 1, 4), '\n')
#
#
# for i in range(1, 8):
#     for j in range(1, 8):
#         if i != j:
#             print("shortest path from ", i, ' to ', j, '=', og.shortest_path(g3, i, j))


graph = og.Graph(g2)

print(f'graph Nodes: \n {graph.nodes_list()}')
print(f'graph Arches: \n {graph.arcs_list()}')
graph.add_node(9)
print(f'graph Nodes: \n {graph.nodes_list()}')
