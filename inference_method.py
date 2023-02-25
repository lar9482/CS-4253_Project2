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
    #Get arcs between the inputted variable and its unassigned variables
    queue = Queue(maxsize=sys.maxsize)
    for neighbor_variable in CSP.get_neighbor_variables(variable):
        if (neighbor_variable in domain.keys()):
            queue.put((neighbor_variable, variable))
    
    while (True):
        
        #If the queue is empty, exit the loop
        if (queue.empty()):
            break

        #Getting the first tail and head pair(X_i, X_j) from the queue
        (X_i, X_j) = queue.get()

        #If the domain of the tail(X_i) was edited, then either fail or add the neighbors to the queue
        if revise(CSP, X_i, X_j, variable, domain):

            #Indication of failure, when the domain of the tail(X_i) is empty
            if (len(domain[X_i]) == 0):
                return "failure"
            
            #For all unassigned neighbors of the tail(X_i), pair it with the tail 
            #and add it to the queue
            for X_k in CSP.get_neighbor_variables(X_i):
                if (X_k != X_j and X_k in domain.keys()):
                    queue.put((X_k, X_i))

    return domain

def revise(CSP, X_i, X_j, variable, domain):
    revise = False

    #Scanning through all current legal values for the tail variable

    #Indication of an arc in-consistency is detected if the last legal value in the head variable(X_j)
    #is equal to the current domain value test from the tail variable(X_i)
    for x in domain[X_i]:
        
        #If the head variable(X_j) happens to the inputted variable in the arc3-method
        if (X_j == variable):
            if (CSP.assignment[variable] == x):
                domain[X_i].remove(x)
                revise = True

        #Else, for everything else, it's in the unassigned variable pool
        else:
            if (len(domain[X_j]) == 1 and domain[X_j][0] == x):
                domain[X_i].remove(x)
                revise = True

    return revise