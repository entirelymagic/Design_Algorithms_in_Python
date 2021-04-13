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


def gradeExtMin(graph):
    """Minimum exterior grade for a graph."""
    min_grade = 100000000
    for node in graph:
        gradeNode = gradeExt(graph, node)
        if gradeNode < min_grade:
            min_grade = gradeNode
    return min_grade


def gradeExtMax(graph):
    """Maximum exterior grade for a graph."""
    max_grade = -1
    for node in graph:
        gradeNode = gradeExt(graph, node)
        if gradeNode > max_grade:
            max_grade = gradeNode
    return max_grade


def gradeIntMin(graph):
    """Minimum exterior grade for a graph."""
    min_grade = 100000000
    for node in graph:
        gradeNode = gradeInt(graph, node)
        if gradeNode < min_grade:
            min_grade = gradeNode
    return min_grade


def gradeIntMax(graph):
    """Maximum exterior grade for a graph."""
    max_grade = -1
    for node in graph:
        gradeNode = gradeInt(graph, node)
        if gradeNode > max_grade:
            max_grade = gradeNode
    return max_grade


def path(graph: dict, start_node: list or tuple, end_node: list or tuple, track: list = None) -> None or list:
    """ Search for the chain(road) between 2 nodes using a similar DF algorithm.
    Will return a list with the track(chain) if there is one or None if there is not a road.

    :param: start_node: the starting node of the oriented graph
    :param: end_node: the ending node of the oriented
    :param: track: the road of the oriented from start to finish(end)
    """

    if track is None:
        track = []

    track = track + [start_node]  # adding the starting node to the track
    if start_node == end_node:  # if the starting node is the ending node
        return track
    if not (start_node in graph):
        return None
    for i in graph[start_node]:
        if i not in track:
            track1 = path(graph, i, end_node, track)  # we use recursive function to start with the new node
            if track1:
                return track1
    return None


def all_paths(graph: dict, start_node: list or tuple, end_node: list or tuple, track: list = None):
    """ Search for all the chains(roads) between 2 nodes using a similar DF algorithm.
    Will return a list with the track(chain) if there is one or None if there is not a road.

    :param: start_node: the starting node of the oriented graph
    :param: end_node: the ending node of the oriented
    :param: track: the road of the oriented from start to finish(end)
    """

    if track is None:
        track = []

    track = track + [start_node]

    if start_node == end_node:  # if the starting node is the ending node
        return [track]

    if not (start_node in graph):
        return []

    tracks = []  # list with all the  tracks
    for i in graph[start_node]:
        if i not in track:
            tracks1 = all_paths(graph, i, end_node, track)  # we use recursive function to start with the new node
            for track1 in tracks1:
                tracks.append(track1)
    return tracks


def shortest_path(graph: dict, start_node: list or tuple, end_node: list or tuple, track: list = None):
    """ Search for the shortest path between 2 nodes.
    Will return a list with the track(chain) if there is one or None if there is not a road.

    :param: start_node: the starting node of the oriented graph
    :param: end_node: the ending node of the oriented
    :param: track: the road of the oriented from start to finish(end)
    """

    if track is None:
        track = []

    track = track + [start_node]

    if start_node == end_node:  # if the starting node is the ending node
        return track

    if not (start_node in graph):
        return None

    shortest_road = None

    for i in graph[start_node]:
        if i not in track:
            track1 = shortest_path(graph, i, end_node, track)  # we use recursive function to start with the new node
            if track1:
                if not shortest_road or len(track1) < len(shortest_road):
                    shortest_road = track1
    return shortest_road


class Graph:
    def __init__(self, graph: dict = None):
        if graph is None:
            graph = {}
        self.__graph = graph

    def nodes_list(self):
        """:return a list from the keys(nodes) of the graph dictionary"""
        return list(self.__graph.keys())

    def arcs_list(self):
        """:return a list of arcs from merhod __get_arches """
        return self.__get_arches()

    def add_node(self, node):
        """if the node is not between the keys of the graph dictionary, it is added adjacent """
        if node not in self.__graph:
            self.__graph[node] = []

    def add_arch(self, arch: list or tuple) -> None:
        """Add an arch (node1, node2) to the graph to the adjacent list, if they are not in the graph keys."""
        [node1, node2] = list(arch)  # get the 2 nodes from the arch
        if node1 not in self.__graph:
            self.__graph[node1] = []
        if node2 not in self.__graph:
            self.__graph[node2] = []
        self.__graph[node1].append(node2)  # add node2 in the adjacent list of node1,

    def __get_arches(self):
        """:return list of arches from the graph"""
        arches_list = []  # initial the list of arches is an empty list
        for node in self.__graph:
            for j in self.__graph[node]:
                if [node, j] not in arches_list:
                    arches_list.append([node, j])
        return arches_list

    def __str__(self):
        """extract all the nodes and arches in info."""
        info = 'Nodes: '
        for node in self.__graph:
            info += str(node) + ' '  # concatenate the nodes to the info
        info += '\nArches'
        for arch in self.__get_arches():
            info += str(arch) + ' '  # concatenate the arches to the info
        return info

