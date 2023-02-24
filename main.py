import json
from utils.file_io import gen_mcp, load_mcp, gen_sudoku, load_sudoku
from csp.mcp_csp import mcp_csp, Color
from order_method import Random_Method, MRV_Method, MRV_Degree_Method
from inference_method import default_method, forward_method, ac3_method
from backtrack import backtrack

mcp_sizes = [10, 50, 100]
mcp_num_instances = 10

sudoku_num_missing = 65
sudoku_num_instances = 100

order_methods = [Random_Method, MRV_Method, MRV_Degree_Method]
inference_methods = [default_method, forward_method, ac3_method]

def generate_mcp():
    for size in mcp_sizes:
        for num in range(1, mcp_num_instances+1):
            file_name = "gcp_{0}_{1}.json".format(size, num)
            gen_mcp(size, file_name)

def generate_sudoku():
    for num in range(1, sudoku_num_instances+1):
        file_name = "sudoku_{0}_{1}".format(sudoku_num_missing, num)
        gen_sudoku(file_name)
def test_mcp():
    size = 100
    # gen_mcp(size)
    mcp_csp = load_mcp()

    test = backtrack(mcp_csp, MRV_Method, ac3_method)
    print()
    for var in range(0, size):
        print(test.constraint_consistent(var, test.assignment[var]))
    print()


def test_sudoku():
    block_size = 3
    # gen_sudoku(81, block_size)
    sudoku_csp = load_sudoku()

    
    result = backtrack(sudoku_csp, MRV_Method, forward_method)
    for row in range(0, block_size ** 2):
        for col in range(0, block_size ** 2):
            print(result.assignment[(row, col)], end=" ")
        print()
    print()


def main():
    # test_mcp()
    # test_sudoku()
    generate_mcp()
    print()
    

if __name__=="__main__":
    main()