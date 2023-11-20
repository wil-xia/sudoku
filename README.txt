# William Xia
# 11/11/23
# Assignment 4: Constraint Satisfaction Problems README

HOW TO RUN:

Open command prompt and switch to the directory containing the sudoku.py
Type python sudoku.py in the command line

The program will automatically run with the example board provided in the
assignment spec. If you wish to run the algorithm on a different board, you
must manually change the hard-coded "initial_board" variable. The harder board
is there as well, but commented out. Simply uncomment it and comment out the
original board if you wish to test it.


ASSUMPTIONS:

This CSP algorithm recursively updates the "initial_board" variable, eventually
over-writing it with the solution at the end of the algorithm.  

This algorithm will attempt to find a solution by using a Depth First Search
with backtracking. It will proceed index by index (rows first, then columns)
to find the first empty slot. It will then check that slot with all of the 
possible values (1-9), and fill it in with the first valid value. From there,
it recursively runs the algorithm on the new board with the newly inserted
value. If the recursive call on the algorithm results in a failure (there are
no valid values for the next empty slot), the original call resets the slot on
the board to 0 and tries the next value.

CSP ATTRIBUTES:

Variables: Each cell in the Sudoku grid is a variable in the CSP.

Domains: The domain for each variable is the set {1, 2, ..., 9}. The algorithm
only checks values 1-9 for a given variable

Constraints: The constraints ensure that no two cells in the same row, column, 
or 3x3 box have the same value.