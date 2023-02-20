def copy_domain(domain):
    copy_domain = {}
    for variable in domain.keys():
        copy_domain[variable] = []
        for domain_value in domain[variable]:
            copy_domain[variable].append(domain_value)

    return copy_domain


def default_method(CSP, variable):    
    return CSP.domain



def forward_method(CSP, variable):
    variable_value = CSP.assignment[variable]
    domain = copy_domain(CSP.domain)

    for neighbor_variable in CSP.get_neighbor_variables(variable):
        if (variable_value in domain[neighbor_variable]):
            domain[neighbor_variable].remove(variable_value)

            if (len(domain[neighbor_variable]) == 0):
                return "failure"
    
    return domain

def ac3_method(CSP, variable):

    print()