import json
from utils.file_io import gen_mcp, load_mcp, gen_sudoku, load_sudoku
from csp.mcp_csp import mcp_csp, Color


def test_mcp():
    # gen_gcp(3)
    mcp_csp = load_mcp()
    print(mcp_csp.get_neighbor_variables(0))
    print(mcp_csp.get_neighbor_variables(1))
    print(mcp_csp.get_neighbor_variables(2))

    mcp_csp.assignment[0] = {Color.R}
    mcp_csp.assignment[1] = {Color.B}
    mcp_csp.assignment[2] = {Color.G}
    print(mcp_csp.constraint_consistent(0))
    print(mcp_csp.constraint_consistent(1))
    print(mcp_csp.constraint_consistent(2))

def test_sudoku():
    gen_sudoku(0)
    load_sudoku()
    print()


def main():
    test_sudoku()
    print()
    

if __name__=="__main__":
    main()