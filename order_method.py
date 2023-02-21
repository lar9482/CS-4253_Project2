import random
import sys

def calculate_MRVs(CSP):
    min_domain_length = sys.maxsize
    min_variables = []
    for variable in CSP.domain.keys():
        if (len(CSP.domain[variable]) < min_domain_length):
            min_domain_length = len(CSP.domain[variable])
            min_variables.clear()

        if (len(CSP.domain[variable]) == min_domain_length):
            min_variables.append(variable)
    
    return min_variables


def Random_Method(CSP):

    #Select a random variable from the domain, without any heuristic
    return (random.choice(list(CSP.domain.keys())))

def MRV_Method(CSP):
    return random.choice(calculate_MRVs(CSP))


def MRV_Degree_Method(CSP):

    MRVs = calculate_MRVs(CSP)
    highestDegree = -sys.maxsize - 1
    highestDegreeVariable = MRVs[0]

    for variable in MRVs:
        num_neighbors = len(CSP.get_neighbor_variables(variable))
        if (num_neighbors > highestDegree):
            highestDegree = num_neighbors
            highestDegreeVariable = variable

    return highestDegreeVariable