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

    #Getting the MRVs(variables with the fewest remaining legal values)
    MRVs = calculate_MRVs(CSP)
    highestDegree = -sys.maxsize - 1
    highestDegreeVariables = []

    #Scanning through all of the MRVs
    for variable in MRVs:

        #For all of the neighbor variables of an MRV, 
        #check if the number of unassigned neighbors is freater than the current degree
        all_neighbors = CSP.get_neighbor_variables(variable)
        num_unassigned_neighbors = 0

        for neighbor_variable in all_neighbors:
            if (neighbor_variable in CSP.domain.keys()):
                num_unassigned_neighbors += 1
        
        #If it's higher, reset the current degree
        if (num_unassigned_neighbors > highestDegree):
            highestDegreeVariables.clear()
            highestDegree = num_unassigned_neighbors

        #If not, keep track of the variable if possible
        if (num_unassigned_neighbors == highestDegree):
            highestDegreeVariables.append(variable)


    #Grab a random variable from MRVs that have the most
    #unassigned neighbor variables
    return random.choice(highestDegreeVariables)