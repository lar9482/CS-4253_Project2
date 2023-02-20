from csp.csp import CSP
from enum import Enum

class Color(Enum):
    R = 1
    G = 2
    B = 3
    Y = 4

class mcp_csp(CSP):
    def __init__(self, data):
        (num_variable, assignment, domain) = self.__initial_num_assignment_domain(data)
        self.edges = data['edges']
        super().__init__(num_variable, assignment, domain)

    def __initial_num_assignment_domain(self, data):
        initial_assignments = {}
        initial_domain = {}
        for variable in data['points']:
            initial_domain[int(variable)] = [Color.R, Color.G, Color.B, Color.Y]
            
        return (data['num_points'], initial_assignments, initial_domain)
    
    

    def get_neighbor_variables(self, variable):
        neighbor_variables = []
        for edge in self.edges:
            if (edge[0] == variable):
                neighbor_variables.append(edge[1])
            elif (edge[1] == variable):
                neighbor_variables.append(edge[0])
        
        return [*set(neighbor_variables)]