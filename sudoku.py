import sys
import numpy as np
import math

def sudoku(plane):
	"Solve the problem line-by-line rather then grid-by-grid"
	zeros_position = searchZeros(plane)
	operators = [1,2,3,4,5,6,7,8,9]

	def recursive_solver(pos):
		if nxt_pos_index >= len(zeros_position):
			return plane
		row, col = zeros_position[pos]
		
		for operator in operators:
			print("row, col: {}, {}".format(row, col))
			print("operator: {}".format(operator))
			plane[row][col] = operator
			if isValidMove(row, col, plane):
				print(plane)
				return recursive_solver(pos+1)
		# backtrack if all operators not fit
		plane[row][col] = 0
		return recursive_solver(pos-1)

	def iterative_solver(pos):
		cache = [1]*len(zeros_position)
		while pos < len(zeros_position):
			#print("********************************")
			if pos < 0:
				print("This puzzle may not be solvable")
				sys.exit(-1)
			row, col = zeros_position[pos]

			for i in range(cache[pos], 10): # x - 9
				plane[row][col] = i
				if isValidMove(row, col, plane):
					cache[pos] = i+1
					pos += 1
					break
			else:
				plane[row][col] = 0
				cache[pos] = 1
				pos -= 1			
		return plane

	startOfZerosIndex = 0 # just for clarafication
	return iterative_solver(startOfZerosIndex)

def searchZeros(plane):
	zero_position = []
	for i, line in enumerate(plane):
		for j, val in enumerate(line):
			if plane[i][j] == 0:
				zero_position.append((i, j))
	return np.array(zero_position)

def isValidMove(row, column, plane):
	checkRow = hasNoDuplicated(plane[row])
	checkCol = hasNoDuplicated(plane[:, column])

	grid = getGrid(row, column, plane)
	checkGrd = hasNoDuplicated(fromGrid2Array(grid))
	return checkRow and checkCol and checkGrd

def hasNoDuplicated(array):
	table = {i:0 for i in range(1, 10)}
	for elem in array:
		if elem == 0: continue
		elif table[elem] >= 1:
			return False
		table[elem] += 1
	return True

def getGrid(row, column, plane):
	row += 1 # They need to plus one, math is not start with 0
	column += 1
	gridRow = math.ceil(row/3) - 1# The i-th grid where i=0,1,2
	gridCol = math.ceil(column/3) - 1

	startOfGrid_row = gridRow * 3
	startOfGrid_col = gridCol * 3

	return plane[
		startOfGrid_row:startOfGrid_row+3, 
		startOfGrid_col:startOfGrid_col+3
	]

fromGrid2Array = lambda grid: grid.flatten() 

def isAllFilled(plane):
	return True if 0 not in plane else False

def file2Numpy(fn):
	ls = []
	with open(fn, 'r') as f:
		for line in f.readlines():
			line = line.replace("\n", "")
			ls.append(list(map(int, line.split())))
	return np.array(ls)

def main():
	print("Input Plane:")
	plane = file2Numpy(fileName)


	print(plane)
	print("Output Plane:")
	output = sudoku(plane)
	print(output)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise ValueError("Please provide the plane file")
    fileName = sys.argv[1]
    main()