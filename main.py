import json
from utils.file_io import gen_mcp, load_mcp, gen_sudoku, load_sudoku
from csp.mcp_csp import mcp_csp, Color
from order_method import random_method
from backtrack import backtrack

def test_mcp():
    gen_mcp(15)
    mcp_csp = load_mcp()

    test = backtrack(mcp_csp)
    print()


def test_sudoku():
    block_size = 3
    # gen_sudoku(25, block_size)
    sudoku_csp = load_sudoku()

    print(random_method(sudoku_csp))
    print()


def main():
    test_mcp()
    # test_sudoku()
    print()
    

if __name__=="__main__":
    main()