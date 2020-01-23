# Name: Gabriel Barney
# Asgn: 2
# Sect: CSC-349-01


from stack_array import * #Needed for Depth First Search
from queue_array import * #Needed for Breadth First Search
import sys

def main():
    
        fp_read = open(sys.argv[1], "r")
        lines = fp_read.readlines()
        lines = [i.strip().split() for i in lines]
        graph = Graph()
        for i in lines:
            graph.add_vertex(i[0])
            graph.add_vertex(i[1])
            graph.add_edge(i[0], i[1])           
        fp_read.close()
        numConnComps = graph.conn_components()
        is_bipartite = graph.is_bipartite()
        if is_bipartite:
            print("Is two-colorable")
        else:
            print("Is not two-colorable")
        print("{0} connected component(s)".format(numConnComps))



class Vertex:
    

    def __init__(self, key):
        self.id = key
        self.adjacent_vertices = []
        self.visited = False
        self.color = None

        
    def add_neighbor(self, key):
        self.adjacent_vertices.append(key)

        
class Graph:
    

    def __init__(self):
        self.vertex_keys = {}   
    
    
    def add_vertex(self, key):
        if key not in self.vertex_keys:
            self.vertex_keys[key] = Vertex(key)       


    def get_vertex(self, key):
        if key in self.vertex_keys:
            return self.vertex_keys[key] 
        return None


    def add_edge(self, v1, v2):
        self.vertex_keys[v1].add_neighbor(v2)
        self.vertex_keys[v2].add_neighbor(v1)


    def get_vertices(self):
        verts = [vert for vert in self.vertex_keys]
        verts = sorted(verts)
        return verts

    
    def conn_components(self):
        stack = Stack(1)
        conn_comps = []
        for vert in self.vertex_keys:
            vert = self.get_vertex(vert)
            vert.visited = False
        for vert in self.vertex_keys:
            vert = self.get_vertex(vert)
            if vert.visited == False:
                stack.push(vert)
                smaller_conns = []
                while stack.is_empty() == False:
                    popped = stack.pop()
                    if popped.visited != True:
                        popped.visited = True
                        smaller_conns.append(popped.id)
                        for adj_vert in popped.adjacent_vertices:
                            adj_vert = self.get_vertex(adj_vert)
                            if adj_vert.visited != True:
                                if stack.is_full():
                                    stack.grow()
                                stack.push(adj_vert)
                sorted_smaller_conns = sorted(smaller_conns)
                conn_comps.append(sorted_smaller_conns)
        return len(conn_comps)


    def is_bipartite(self):
        queue = Queue(10000)
        for vert in self.vertex_keys:
            vert = self.get_vertex(vert)
            vert.visited = False
            vert.color = None
        for vert in self.vertex_keys:
            vert = self.get_vertex(vert)
            for adj_vert in vert.adjacent_vertices:
                adj_vert = self.get_vertex(adj_vert)
                adj_vert.visited = False
            queue.enqueue(vert)
            while queue.is_empty() == False:
                current_vert = queue.dequeue()
                current_vert.visited = True
                if current_vert.color == None:
                    current_vert.color = 1
                not_visited = self.get_not_visited(adj_vert, current_vert)
                for adj_vertex in not_visited:
                    adj_vertex.visited = True
                    if adj_vertex.color != None:
                        if adj_vertex.color != -current_vert.color:
                            return False
                    else:
                        adj_vertex.color = -current_vert.color
                    queue.enqueue(adj_vertex)
        return True
                        

    def get_not_visited(self, adj_vert, current_vert):
        """Helper function that returns the adjacent vertices to the current vertex
        that have yet to be visited so they may be marked as visited."""
        not_visited = []
        for adj_vert in current_vert.adjacent_vertices:
            adj_vert = self.get_vertex(adj_vert)
            if adj_vert.visited == False:
                not_visited.append(adj_vert)
        return not_visited

if __name__ == "__main__":
    main()
