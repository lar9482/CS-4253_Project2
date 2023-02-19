import json
from utils.file_io import gen_mcp, load_mcp, gen_sudoku, load_sudoku
from csp.mcp_csp import mcp_csp, Color


def test_mcp():
    # gen_gcp(3)
    mcp_csp = load_mcp()
    print(mcp_csp.get_neighbor_variables(0))
    print(mcp_csp.get_neighbor_variables(1))
    print(mcp_csp.get_neighbor_variables(2))

    mcp_csp.assignment[0] = Color.B
    mcp_csp.assignment[1] = Color.R
    print(mcp_csp.constraint_consistent(2, Color.B))
    print(mcp_csp.constraint_consistent(2, Color.G))


def test_sudoku():
    block_size = 3
    # gen_sudoku(0, block_size)
    sudoku_csp = load_sudoku()
    # for i in range(0, block_size**2):
    #     sudoku_csp.get_neighbor_variables((i, i))

    test = sudoku_csp.get_neighbor_variables((0, 0))
    print(sudoku_csp.constraint_consistent((0, 0), 7))


    print()


def main():
    # test_mcp()
    test_sudoku()
    print()
    

if __name__=="__main__":
    main()