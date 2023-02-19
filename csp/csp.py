from abc import ABC, abstractmethod

class CSP:
    def __init__(self, num_variables, assignment, domain):
        self.num_variables = num_variables
        self.assignment = assignment
        self.domain = domain

    def constraint_consistent(self, variable):
        #Checks if the variable has been assigned yet
        if (self.assignment[variable] is not None):
            neighbor_variables = self.get_neighbor_variables(variable)

            for neighbor in neighbor_variables:
                if (self.assignment[neighbor] is not None):
                    if (self.assignment[variable] == self.assignment[neighbor]):
                        return False
        return True

    @abstractmethod
    def get_neighbor_variables(self, variable):
        pass