import json
import os
import sys
import time
from utils.file_io import gen_mcp, load_mcp, gen_sudoku, load_sudoku, save_mcp_runtimes, save_sudoku_runtimes
from csp.mcp_csp import mcp_csp, Color
from order_method import Random_Method, MRV_Method, MRV_Degree_Method
from inference_method import default_method, forward_method, ac3_method
from backtrack import backtrack

from multiprocessing import Process, Manager


def generate_mcp(mcp_sizes, mcp_num_instances):
    for size in mcp_sizes:
        for num in range(1, mcp_num_instances+1):
            file_name = "gcp_{0}_{1}.json".format(size, num)
            file_name = os.path.join(sys.path[0], 'mcp_data', file_name)
            gen_mcp(size, file_name)

def generate_sudoku(sudoku_num_missing, sudoku_num_instances):
    for num_missing in sudoku_num_missing:
        for num in range(1, sudoku_num_instances+1):
            file_name = "sudoku_{0}_{1}.json".format(num_missing, num)
            file_name = os.path.join(sys.path[0], 'sudoku_data', file_name)
            gen_sudoku(num_missing, 3, file_name)

def run_mcp(curr_size, curr_instance, order_method, inference_method, 
            shared_time_dict, lock):
    
    #Formatting the input .json filepath based on the current size and instance
    file_name = "gcp_{0}_{1}.json".format(curr_size, curr_instance)
    file_name = os.path.join(sys.path[0], 'mcp_data', file_name)
    
    #Loading in the file
    mcp_csp = load_mcp(file_name)

    #Performing the backtracking
    startTime = time.time()
    backtrack(mcp_csp, order_method, inference_method)
    endTime = time.time()
    
    #Store the total runtime in the shared dictionary
    lock.acquire()
    if (not str((order_method.__name__, inference_method.__name__)) in shared_time_dict):
        shared_time_dict[str((order_method.__name__, inference_method.__name__))] = endTime - startTime
    else:
        shared_time_dict[str((order_method.__name__, inference_method.__name__))] += endTime - startTime
    lock.release()
    
def run_sudoku(num_missing, num_instance, order_method, inference_method,
               shared_time_dict, lock):
    file_name = "sudoku_{0}_{1}.json".format(num_missing, num_instance)
    file_name = os.path.join(sys.path[0], 'sudoku_data', file_name)
    sudoku_csp = load_sudoku(file_name)

    startTime = time.time()
    backtrack(sudoku_csp, order_method, inference_method)
    endTime = time.time()

    lock.acquire()
    if (not str((order_method.__name__, inference_method.__name__)) in shared_time_dict):
        shared_time_dict[str((order_method.__name__, inference_method.__name__))] = endTime - startTime
    else:
        shared_time_dict[str((order_method.__name__, inference_method.__name__))] += endTime - startTime
    lock.release()

def test_mcp(mcp_sizes, mcp_num_instances, order_methods, inference_methods):

    #For all of the specified sizes, run a multi-threaded pool test
    for mcp_size in mcp_sizes:

        #Creating a new manager pool
        with Manager() as manager:
            all_processes = []
            lock = manager.Lock()
            shared_time_dict = manager.dict()

            #For every 'mcp_num_instance', order_method, and inference_method combination,
            #Create a new subprocess
            for num_instance in range(1, mcp_num_instances+1):
                for order_method in order_methods:
                    for inference_method in inference_methods:
                        
                        process = Process(target=run_mcp, args=(
                            mcp_size,
                            num_instance,
                            order_method,
                            inference_method,
                            shared_time_dict,
                            lock
                        ))

                        all_processes.append(process)

            #Start all of the subprocesses
            for process in all_processes:
                process.start()

            #Wait for all subprocesses to finish before continuing
            for process in all_processes:
                process.join()

            time_dict = dict(shared_time_dict)

            #Getting the average of the runtimes
            for order_inference_pair in time_dict.keys():
                time_dict[order_inference_pair] = time_dict[order_inference_pair] / mcp_num_instances

            #Save runtimes to an excel spreadsheet
            save_mcp_runtimes(time_dict, mcp_size)


def test_sudoku(sudoku_num_missing, sudoku_num_instances, order_methods, inference_methods):
    # block_size = 3
    # # gen_sudoku(81, block_size)
    # sudoku_csp = load_sudoku()

    
    # result = backtrack(sudoku_csp, MRV_Degree_Method, forward_method)
    # for row in range(0, block_size ** 2):
    #     for col in range(0, block_size ** 2):
    #         print(result.assignment[(row, col)], end=" ")
    #     print()
    # print()

    for num_missing in sudoku_num_missing:

        chunk_size = 20
        curr_num_instance = chunk_size
        total_dict = {}
        while(curr_num_instance <= sudoku_num_instances):
            
            with Manager() as manager:
                all_processes = []
                lock = manager.Lock()
                shared_time_dict = manager.dict()

                for num_instance in range(curr_num_instance-chunk_size+1, curr_num_instance+1):
                    for order_method in order_methods:
                        for inference_method in inference_methods:
                            # run_sudoku(num_missing, num_instance, order_method, inference_method, shared_time_dict)
                            process = Process(target=run_sudoku, args=(
                                num_missing,
                                num_instance,
                                order_method,
                                inference_method,
                                shared_time_dict,
                                lock
                            ))

                            all_processes.append(process)
                
                #Start all of the subprocesses
                for process in all_processes:
                    process.start()

                #Wait for all subprocesses to finish before continuing
                for process in all_processes:
                    process.join()

                curr_dict = dict(shared_time_dict)

                for order_inference_pair in curr_dict.keys():
                    if (not order_inference_pair in total_dict):
                        total_dict[order_inference_pair] = curr_dict[order_inference_pair]
                    else:
                        total_dict[order_inference_pair] += curr_dict[order_inference_pair]

            curr_num_instance += chunk_size
        
        for order_inference_pair in total_dict.keys():
            total_dict[order_inference_pair] = total_dict[order_inference_pair] / sudoku_num_instances

        save_sudoku_runtimes(total_dict, num_missing)

def main():

    #MCP parameters
    mcp_sizes = [10, 20, 30]
    mcp_num_instances = 10

    #Sudoku parameters
    sudoku_num_missing = [10, 20, 30, 40]
    sudoku_num_instances = 100

    #The types of heuristics that are available
    order_methods = [MRV_Method, MRV_Degree_Method]
    inference_methods = [forward_method, ac3_method]

    
    # generate_mcp(mcp_sizes, mcp_num_instances)
    # generate_sudoku(sudoku_num_missing, sudoku_num_instances)
    test_mcp(mcp_sizes, mcp_num_instances, order_methods, inference_methods)
    # test_sudoku(sudoku_num_missing, sudoku_num_instances, order_methods, inference_methods)
    

if __name__=="__main__":
    main()