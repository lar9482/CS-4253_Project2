from csp.csp import CSP
import math

class sudoku_csp(CSP):
    def __init__(self, board):
        self.block_size = int(math.sqrt(len(board)))
        (assignment, domain) = self.__initial_assignment_domain(board)

        super().__init__(int(self.block_size ** 2), assignment, domain)

    def __initial_assignment_domain(self, board):
        initial_assignments = {}
        initial_domain = {}

        for row in range(0, int(self.block_size ** 2)):
            for col in range(0, int(self.block_size ** 2)):
                if (board[row][col] == 0):
                    initial_domain[(row, col)] = []
                    for domain in range(1, int(self.block_size ** 2)+1):
                        initial_domain[(row, col)].append(domain)
                else:
                    initial_assignments[(row, col)] = board[row][col]

        return (initial_assignments, initial_domain)
    
    def get_neighbor_variables(self, variable):
        curr_row = variable[0]
        curr_col = variable[1]

        neighbor_variables = []

