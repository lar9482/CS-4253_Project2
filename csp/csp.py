from abc import ABC, abstractmethod
from enum import Enum

class Order(Enum):
    Random = 0
    MRV = 1
    MRV_Degree = 2

class Inference(Enum):
    Default = 0
    Forward = 1
    Arc_3 = 2
    
class CSP:
    def __init__(self, num_variables, assignment, domain):
        self.num_variables = num_variables
        self.assignment = assignment
        self.domain = domain

    def constraint_consistent(self, variable, variable_value):
        neighbor_variables = self.get_neighbor_variables(variable)

        for neighbor in neighbor_variables:
            if (self.assignment[neighbor] is not None):
                if (variable_value == self.assignment[neighbor]):
                    return False
        return True
    
    def is_complete(self):
        return len(self.assignment.keys()) == (self.num_variables)

    @abstractmethod
    def get_neighbor_variables(self, variable):
        pass