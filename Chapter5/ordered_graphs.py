def arches(graph: dict) -> list:
    """return a list of arcs given a dictionary as a graph"""
    arcs_list = []  # initial list of arcs
    for i in graph:
        for j in graph[i]:
            arcs_list.append((i, j))
    return arcs_list


def gradeExt(graph: dict, node: tuple):
    """exterior grade of a node in a oriented graph"""
    grade = len(graph[node])
    return grade


def gradeInt(graph: dict, node: tuple):
    """interior grade of a node in a oriented graph"""
    grade = 0
    for i in graph:
        if node in graph[i]:  # if the arch exists(i, node)
            grade += 1
    return grade


def isolateDiGraph(graph):
    """return isolated nodes given a graph"""
    list_isolated = []
    isolated = False
    for node in graph:
        if not graph[node]:
            isolated = True
        for i in graph:
            if node in graph[i]:
                isolated = False
            if isolated:
                list_isolated += [node]
    return list_isolated
