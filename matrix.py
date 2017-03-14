from sys import stdout, exit

def create_matrix_with_str_arg(y, x, coefficients):
	if (y * x < len(coefficients)):
		print("Too much coefficients for a matrix of size "+str(y), str(x)+"\nPlease put at max "+str(x*y)+" arguments.")
		exit(84)
	try:
		str(coefficients)
	except:
		print("please enter a string as third parameter")
		exit(84)
	mat = [[0] * x for _ in range(y)]
	k = 0
	for i in range(y):
		for j in range(x):
			mat[i][j] = int(coefficients[k])
			k += 1
	return (mat)

def create_matrix(y, x, filler):
	return [[filler] * x for _ in range(y)]

def identity_matrix(length):
	m = create_matrix(length, length, 0)
	for i in range(len(m)):
		m[i][i] = 1
	return (m)

def print_matrix(mat):
	for i in range(len(mat)):
		for j in range(len(mat[i])):
			if (j + 1 != len(mat[i])):
				stdout.write(str(mat[i][j]) + "\t")
			else:
				stdout.write(str(mat[i][j]))
		stdout.write("\n")

def multiply_matrix(mat1, mat2):
	if (len(mat1[0]) != len(mat2)):
		print("Can't multiply matrix with different length in mat1 x and mat 2 y")
		return (-1)
	result = create_matrix(len(mat1), len(mat2[0]), 0)
	k = 0
	for i in range(len(mat1)):
		for j in range(len(mat2[0])):
			for l in range(len(mat1[0])):
				result[i][j] += mat1[i][l] * mat2[l][j]
	return (result)

def add_matrix(mat1, mat2):
	matrix = create_matrix(len(mat1), len(mat1[0]), 0)
	for i in range(len(mat1)):
		for j in range(len(mat1[0])):
			matrix[i][j] = mat1[i][j] + mat2[i][j]
	return (matrix)

def substract_matrix(mat1, mat2):
	matrix = create_matrix(len(mat1), len(mat1[0]), 0)
	for i in range(len(mat1)):
		for j in range(len(mat1[0])):
			matrix[i][j] = mat1[i][j] - mat2[i][j]
	return (matrix)

def multiply_matrix_by_one_number(number, matrix):
	tmp = len(matrix)
	tmp2 = len(matrix[0])
	res = create_matrix(len(matrix), len(matrix[0]), 0)
	for i in range(tmp):
		for j in range(tmp2):
			res[i][j] = number * matrix[i][j]
	return (res)

def divide_matrix_by_one_number(number, matrix):
	res = create_matrix(len(matrix), len(matrix[0]), 0)
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			res[i][j] = matrix[i][j] / number
	return (res)

def pow_matrix(matrix, n):
	tmp = matrix
	i = 1
	while (i < n):
		matrix = multiply_matrix(matrix, tmp)
		i += 1
	return (matrix)
