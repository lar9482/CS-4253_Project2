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

        #Scanning through all of the rows and columns for the board
        for row in range(0, int(self.block_size ** 2)):
            for col in range(0, int(self.block_size ** 2)):

                #A zero indicates an unassigned variable initially
                #Place it into the 'domains'
                if (board[row][col] == 0):
                    initial_domain[(row, col)] = []
                    for domain in range(1, int(self.block_size ** 2)+1):
                        initial_domain[(row, col)].append(domain)

                #Else, place the variable into the assignments
                else:
                    initial_assignments[(row, col)] = board[row][col]

        return (initial_assignments, initial_domain)
    
    def get_neighbor_variables(self, variable):
        curr_row = variable[0]
        curr_col = variable[1]

        neighbor_variables = []

        #Getting the row neighbors
        for col in range(0, self.block_size ** 2):
            if (col == curr_col):
                continue
            neighbor_variables.append((curr_row, col))

        #Getting the column neighbors
        for row in range(0, self.block_size ** 2):
            if (row == curr_row):
                continue
            neighbor_variables.append((row, curr_col))

        #Getting the region neighbors
        regionRowStart = int((curr_row) / self.block_size)*self.block_size
        regionColStart = int((curr_col) / self.block_size)*self.block_size

        for regionRow in range(regionRowStart, regionRowStart+self.block_size):
            for regionCol in range(regionColStart, regionColStart+self.block_size):
                if (regionRow == curr_row and regionCol == curr_col):
                    continue
                neighbor_variables.append((regionRow, regionCol))

        return neighbor_variables

