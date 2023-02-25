from abc import ABC, abstractmethod

class CSP:
    def __init__(self, num_variables, assignment, domain):
        self.num_variables = num_variables
        #A dictionary of variable/value pairs
        self.assignment = assignment

        #A dictionary of variable/legal-value pairs
        self.domain = domain

    def constraint_consistent(self, variable, variable_value):

        #Getting all possible neighbor variables of the inputted variable
        neighbor_variables = self.get_neighbor_variables(variable)

        #Scanning through all neighbors
        for neighbor in neighbor_variables:
            #If the neighbor is present in the assignment dictionary,
            #and its assigned value is equal is equal to the inputted variable value,
            #then an inconsistency has been found
            if (neighbor in self.assignment):
                if (variable_value == self.assignment[neighbor]):
                    return False
        return True
    
    def is_complete(self):

        #If the number of variables in the assignment dictionary is equal to the total number of variables,
        #then an complete assignment has been reached
        return len(self.assignment.keys()) == (self.num_variables)

    @abstractmethod
    def get_neighbor_variables(self, variable):
        pass