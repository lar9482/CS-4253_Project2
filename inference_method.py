from queue import Queue
import sys

def copy_domain(domain):
    copy_domain = {}

    #Create a deep copy of the domain
    for variable in domain.keys():
        copy_domain[variable] = []
        for domain_value in domain[variable]:
            copy_domain[variable].append(domain_value)

    return copy_domain

def default_method(CSP, variable):    
    return CSP.domain

def forward_method(CSP, variable):
    variable_value = CSP.assignment[variable]

    #Get a deep copy of the domain of the CSP
    domain = copy_domain(CSP.domain)

    #Scanning through all of the neighbor variables of 'variable
    for neighbor_variable in CSP.get_neighbor_variables(variable):

        #If the variable value is present in the neighbor, then remove it
        if (neighbor_variable in domain.keys() and variable_value in domain[neighbor_variable]):
            domain[neighbor_variable].remove(variable_value)

            #An empty domain indicates a failure
            if (len(domain[neighbor_variable]) == 0):
                return "failure"
    
    return domain

def ac3_method(CSP, variable):

    #Get a deep copy of the CSP's domain
    domain = copy_domain(CSP.domain)

    #Calculate initial arcs
    #Get arcs between the inputted variables and its unassigned variables
    queue = Queue(maxsize=sys.maxsize)
    for neighbor_variable in CSP.get_neighbor_variables(variable):
        if (neighbor_variable in domain.keys()):
            queue.put((neighbor_variable, variable))
    
    while (True):
        
        if (queue.empty()):
            break

        (X_i, X_j) = queue.get()

        if revise(CSP, X_i, X_j, variable, domain):
            if (len(domain[X_i]) == 0):
                return "failure"
            
            for X_k in CSP.get_neighbor_variables(X_i):
                if (X_k != X_j and X_k in domain.keys()):
                    queue.put((X_k, X_i))

    return domain

def revise(CSP, X_i, X_j, variable, domain):
    revise = False
    for x in domain[X_i]:
        
        if (X_j == variable):
            if (CSP.assignment[variable] == x):
                domain[X_i].remove(x)
                revise = True
        else:
            if (len(domain[X_j]) == 1 and domain[X_j][0] == x):
                domain[X_i].remove(x)
                revise = True

    return revise