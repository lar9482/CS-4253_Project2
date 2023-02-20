import json
from utils.file_io import gen_mcp, load_mcp, gen_sudoku, load_sudoku
from csp.mcp_csp import mcp_csp, Color
from order_method import random_method
from backtrack import backtrack

def test_mcp():
    size = 30
    gen_mcp(size)
    mcp_csp = load_mcp()

    test = backtrack(mcp_csp)

    for var in range(0, size):
        print(test.constraint_consistent(var, test.assignment[var]))
    print()


def test_sudoku():
    block_size = 3
    gen_sudoku(40, block_size)
    sudoku_csp = load_sudoku()

    result = backtrack(sudoku_csp)
    for row in range(0, block_size ** 2):
        for col in range(0, block_size ** 2):
            print(result.assignment[(row, col)], end=" ")
        print()
    print()


def main():
    # test_mcp()
    test_sudoku()
    print()
    

if __name__=="__main__":
    main()