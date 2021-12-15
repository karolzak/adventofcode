import numpy as np
from collections import defaultdict

class Graph:
    def __init__(self, cave):
        self.v = cave.shape[0] * cave.shape[1]
        self.cave = cave

    @staticmethod
    def get_neighbours(current_node, max_indices):

        neighbours = []
        i, j = current_node
        i_max, j_max = max_indices

        if i > 0: neighbours.append((i-1, j))
        if i < i_max: neighbours.append((i+1, j))        
        if j > 0: neighbours.append((i, j-1))
        if j < j_max: neighbours.append((i, j+1))

        return neighbours

    def get_neighbours_dict(self):

        neighbours_dict = defaultdict(list)
        x_max, y_max = self.cave.shape

        for i in range(0, x_max):
            for j in range(0, y_max):
                neighbours_dict[(i, j)] = self.get_neighbours((i, j), (x_max-1, y_max-1))

        return neighbours_dict

    def extend_cave(self, nb_tile):

        x_max, y_max = self.cave.shape
        new_cave = np.zeros((x_max*nb_tile, y_max*nb_tile))

        new_cave[0:x_max, 0:y_max] = self.cave

        max_add = 2*nb_tile-1
        m = self.cave
        for add_val in range(1, max_add):
            m = np.ones((x_max, y_max)) + m
            m = np.where(m>9, 1, m)
            for i in range(0, nb_tile):
                for j in range(0, nb_tile):
                    if i + j == add_val:
                        new_cave[i*x_max:(i+1)*x_max, j*y_max:(j+1)*y_max] = m
        
        self.cave = new_cave
    
    def find_shortest_path(self):
        """
        Implementing Dijkstra's algorithm for the shortest path
        """
        x_max, y_max = self.cave.shape
        dist = float('inf') * np.ones((x_max, y_max))
        neighbours = self.get_neighbours_dict()

        queue = []
        current_node = (0, 0)
        queue.append((0, current_node))
        dist[current_node] = 0
        visited = set()

        while queue:
            queue = sorted(queue)
            current_node = queue.pop(0)[1]
            visited.add(current_node)

            for neighbour in neighbours[current_node]:
                if neighbour not in visited:
                    old_cost = dist[neighbour]
                    new_cost = dist[current_node] + self.cave[neighbour]
                    if new_cost < old_cost:
                        dist[neighbour] = new_cost
                        queue.append((dist[neighbour], neighbour))

        return dist


if __name__ == '__main__':
    file = open('15-input.txt', 'r')
    lines = [line.strip() for line in file.readlines()]   

    cave = np.array([[int(char) for char in line] for line in lines])
    graph = Graph(cave)
    D = graph.find_shortest_path()
    bottom_right_node = (cave.shape[0]-1, cave.shape[1]-1)
    
    print("Answer to first puzzle: ", D[bottom_right_node])    
    graph.extend_cave(5)
    D = graph.find_shortest_path()
    bottom_right_node = (graph.cave.shape[0]-1, graph.cave.shape[1]-1)

    print("Answer to second puzzle:", D[bottom_right_node])