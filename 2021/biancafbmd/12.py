import numpy as np

from collections import defaultdict, Counter
import pprint

class Graph:
    def __init__(self, graph = None):
        if graph is None:
            graph = defaultdict(list)
        self.graph = graph
    
    def create_graph_from_lines(self,lines):
        for line in lines:
            v = line.split('-')
            self.graph[v[0]].append(v[1])
            self.graph[v[1]].append(v[0])

    def print(self):
        pprint.pprint(self.graph)

    def find_all_paths_lower_cond(self, start='start', end='end', visited = [], cond = False):

        visited = visited + [start]    

        if start == end:
            return [visited]

        paths = []                
        for node in self.graph[start]:
            if graph.check_cave_condition(visited, node, cond):
                found_paths = self.find_all_paths_lower_cond(node, end, visited, cond)
                for path in found_paths:
                    paths.append(path)

        return paths

    @staticmethod
    def check_cave_condition(visited, cave, cond):

        if cave.isupper():
            return True

        if cave == 'start':
            return False

        if cond:
            v_counter = Counter(visited)
            if cave not in v_counter:
                return True
            elif v_counter[cave] >=2:
                return False
            else:
                for element in v_counter:
                    if element.islower() and v_counter[element] >=2:
                        return False
                return True
        else:
            if cave.islower() and cave in visited:
                return False
            else:
                return True

if __name__ == '__main__':
    file = open('12-input.txt', 'r')
    lines = [line.strip() for line in file.readlines()]
    
    graph = Graph()
    graph.create_graph_from_lines(lines)
    #graph.print()
    paths = graph.find_all_paths_lower_cond(cond=False)

    print("Answer to first puzzle: ", len(paths))

    paths = graph.find_all_paths_lower_cond(cond=True)

    print("Answer to second puzzle: ", len(paths))