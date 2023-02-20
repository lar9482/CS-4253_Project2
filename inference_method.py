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
        if (variable_value in domain[neighbor_variable]):
            domain[neighbor_variable].remove(variable_value)

            #An empty domain indicates a failure
            if (len(domain[neighbor_variable]) == 0):
                return "failure"
    
    return domain

def ac3_method(CSP, variable):

    print()