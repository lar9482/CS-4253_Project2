import random
import sys

def calculate_MRVs(CSP):
    min_domain_length = sys.maxsize
    min_variables = []

    #Scanning through all of the unassigned variables in CSP
    for variable in CSP.domain.keys():
        #If the number of remaining legal values of 'variable' is less than
        #the current minimum length, reset progress
        if (len(CSP.domain[variable]) < min_domain_length):
            min_domain_length = len(CSP.domain[variable])
            min_variables.clear()

        #Else, simply append the variable to the min_variables
        if (len(CSP.domain[variable]) == min_domain_length):
            min_variables.append(variable)
    
    return min_variables


def Random_Method(CSP):

    #Select a random variable from the domain, without any ordering heuristic
    return (random.choice(list(CSP.domain.keys())))

def MRV_Method(CSP):
    #Get a random variable from the 'MRVs'
    return random.choice(calculate_MRVs(CSP))


def MRV_Degree_Method(CSP):

    MRVs = calculate_MRVs(CSP)
    highestDegree = -sys.maxsize - 1
    highestDegreeVariables = []

    for variable in MRVs:
        num_neighbors = len(CSP.get_neighbor_variables(variable))
        if (num_neighbors > highestDegree):
            highestDegree = num_neighbors
            highestDegreeVariables.clear()
        

    return highestDegreeVariables