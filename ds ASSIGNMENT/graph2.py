class graph:
    class vertex:
        def __init__(self,node):
            self.vertex_id = node
            self.adjacent = {}
            
        def neighbour_present(self,node):
            return node in self.adjacent
        
        def add_neighbour(self,node,weight=0):
            if not neighbour_present(node):
                self.adjacent[node] = weight
                
        def get_neighbours(self):
            return self.adjacent.keys()
        
        def get_weight(self,node):
            if neighbour_present(node):
                return self.adjacent[node]
    def __init__(self):
        self.vertex_count=0
        self.adjacency_list = {}
        
    def is_empty:
        return self.vertex_count==0
    
    def vertex_present(self,node):
        return node in self.adjacency_list
    
    def add_vertex(self,node):
        if not vertex_present(node):
            self.vertex_count+=1
            new_vertex = vertex(node)
            self.adjacency_list[node]=new_vertex
            
    def add_edge(self,frm,to,cost=0):
        if not vertex_present(frm):
            self.add_vertex(frm)
        if not vertex_present(to):
            self.add_vertex(to)
            self.adjacency_list[frm].add_neighbour(to,cost)
            self.adjacency_list[to].add_neighbour(frm,cost)
            
    def get_neighbours(self, node):
        if self.vertex_present(node):
            self.adjacency_list[node].get_neighbours()
    
            
