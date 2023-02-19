import json
from utils.file_io import gen_gcp, load_gcp
from csp.gcp_csp import gcp_csp, Color

def main():
    print()
    # gen_gcp()
    gcp_csp = load_gcp()
    print(gcp_csp.get_neighbor_variables(0))




if __name__=="__main__":
    main()