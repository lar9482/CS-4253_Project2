from csp.mcp_csp import mcp_csp
from order_method import Random_Method
from inference_method import default_method
import os

def backtrack(CSP = mcp_csp, Order_Method = Random_Method, Inference_Method = default_method):

    #Testing if CSP has assigned all variables
    if CSP.is_complete():
        return CSP
    
    #Getting an unassigned variable based on the requested ordering heuristic
    variable = Order_Method(CSP)

    print('%s working on variable %s' % (str((Order_Method.__name__, Inference_Method.__name__)), str(variable)))

    #Scanning through all of the possible domains of the selected variable
    for domain_value in CSP.domain[variable]:

        #Testing if possible domain_value is consistent with selected variable's neighbors
        #(i.e if domain_value != variable's neighbors that have been assigned)
        if CSP.constraint_consistent(variable, domain_value):

            #Add {var = value} to assignment
            curr_var_domain = CSP.domain[variable]
            CSP.domain.pop(variable) #Removing 'variable' from the domain
            CSP.assignment[variable] = domain_value #Adding 'variable' to assignment

            #Edit the domain of CSP based on the requested inference heuristic
            inference_domains = Inference_Method(CSP, variable)
            if (inference_domains != "failure"):
                #Add inferences to CSP
                previous_domains = CSP.domain #Keeping a copy of the previous domain if a failure happens
                CSP.domain = inference_domains

                #Make a backtrack
                result = backtrack(CSP, Order_Method, Inference_Method)

                #If a complete assignment is detected, then immediately return
                if result != "failure":
                    return result
                
                #Remove inferences from CSP
                CSP.domain = previous_domains

            # Remove {var = value} from assignment
            CSP.domain[variable] = curr_var_domain #Adding 'variable' back to the domain
            CSP.assignment.pop(variable) # Removing 'variable' from assignment

    return "failure"