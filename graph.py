from collections import defaultdict


class Graph(object):
    """ Graph data structure, undirected by default. """

    def __init__(self, connections, directed=False):
        self.algo = "este"
        self._graph = defaultdict(lambda: {"value":0,"edges":set()})
        self._directed = directed
        self.add_connections(connections)

    def add_connections(self, connections):
        """ Add connections (list of tuple pairs) to graph """

        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        """ Add connection between node1 and node2 """

        self._graph[node1]["edges"].add(node2)
        if not self._directed:
            self._graph[node2]["edges"].add(node1)

    def remove(self, node):
        """ Remove all references to node """

        for n, cxns in self._graph.items():  # python3: items(); python2: iteritems()
            try:
                cxns["edge"].remove(node)
            except KeyError:
                pass
        try:
            del self._graph[node]["edges"]
        except KeyError:
            pass

    def is_connected(self, node1, node2):
        """ Is node1 directly connected to node2 """

        return node1 in self._graph and node2 in self._graph[node1]["edges"]

    def find_path(self, node1, node2, path=[]):
        """ Find any path between node1 and node2 (may not be shortest) """

        path = path + [node1]["edges"]
        if node1 == node2:
            return path
        if node1 not in self._graph:
            return None
        for node in self._graph[node1]["edges"]:
            if node not in path:
                new_path = self.find_path(node, node2, path)
                if new_path:
                    return new_path
        return None

    def get_neighbors(self, node):
        return self._graph[node]["edges"]
    
    def get_value(self, node):
        return self._graph[node]["value"]
    
    def set_value(self, node, value):
        self._graph[node]["value"] = value
    
    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))