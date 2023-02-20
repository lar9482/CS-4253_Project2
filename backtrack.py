from csp.mcp_csp import mcp_csp
from order_method import Random_Method
from inference_method import default_method

def backtrack(CSP = mcp_csp, Order_Method = Random_Method, Inference_Method = default_method):
    if CSP.is_complete():
        return CSP
    
    variable = Order_Method(CSP)
    print('Variable: %s' % str(variable))
    for domain_value in CSP.domain[variable]:
        if CSP.constraint_consistent(variable, domain_value):
            #Add {var = value} to assignment
            curr_var_domain = CSP.domain[variable]
            CSP.domain.pop(variable) #Removing 'variable' from the domain
            CSP.assignment[variable] = domain_value #Adding 'variable' to assignment

            inference_domains = Inference_Method(CSP, variable)
            if (inference_domains != "failure"):
                #Add inferences to CSP
                previous_domains = CSP.domain
                CSP.domain = inference_domains

                result = backtrack(CSP, Order_Method, Inference_Method)
                if result != "failure":
                    return result
                
                #Remove inferences from CSP
                CSP.domain = previous_domains

            # Remove {var = value} from assignment
            CSP.domain[variable] = curr_var_domain #Adding 'variable' back to the domain
            CSP.assignment.pop(variable) # Removing 'variable' from assignment

    return "failure"