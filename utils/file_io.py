import json
import random
from utils.gen_gcp import draw, gen
from utils.sudoku_generator import make_board
from csp.mcp_csp import mcp_csp
from csp.sudoku_csp import sudoku_csp

import pandas as pd
import os
import sys

#This function is the starter function from 'gcp_csp', 
# which will generate a map color problem
def gen_mcp(num_points = 10, file_path = 'gcp.json'):
    print("Generating a planar graph with {} points...".format(num_points))
    (x, lines) = gen(num_points=num_points)
    # draw(x, lines)

    print("Writing to '{}'...".format(file_path))
    with open(file_path, 'w') as f:
        f.write(json.dumps({
            'num_points': len(x),
            'points': { p.id: (p.x, p.y) for p in x },
            'edges': [ (line.p1.id, line.p2.id) for line in lines ]
        }, indent=2))
    print("""Done! You can now import the results into a Python script with the code:

import json

with open('{}', r) as f:
    data = json.load(f)
""".format(file_path))


def gen_sudoku(num_missing = 50, block_size = 3, output_file = 'sudoku.json'):
    board = make_board(block_size)

    ms = int(pow(block_size, 2))
    indices = random.sample(list(range(ms * ms)), num_missing)
    for index in indices:
        r = int(index / ms)
        c = int(index % ms)
        board[r][c] = 0

    ## Write to file
    with open(output_file, 'w') as f:
        f.write(json.dumps(board))

#     print("""Board written to '{0}'.

# To read the file with Python, use the code:

# import json
# with open('{0}', 'r') as f:
#     board = json.load(f)
# """.format(output_file))

####################################################################3
#Custom code below for loading CSPs

def load_mcp(file_path = 'gcp.json'):
    with open(file_path, 'r') as f:
        data = json.load(f)
        return mcp_csp(data)
    
def load_sudoku(file_path = 'sudoku.json'):
    with open(file_path, 'r') as f:
        board = json.load(f)
        # for row in range(0, len(board)):
        #     for col in range(0, len(board)):
        #         print(board[row][col], end=" ")
        #     print()
        # print()
        return sudoku_csp(board)
    
def save_mcp_runtimes(time_dict, size):    
    df = pd.DataFrame.from_dict(time_dict.items())
    file_name = os.path.join(sys.path[0], 'mcp_results', 'mcp_{0}'.format(size)) + '.xlsx'
    df.to_excel(file_name)


def save_sudoku_runtimes(time_dict, num_missing):
    df = pd.DataFrame.from_dict(time_dict.items())
    file_name = os.path.join(sys.path[0], 'sudoku_results', 'sudoku_{0}'.format(num_missing)) + '.xlsx'
    df.to_excel(file_name)