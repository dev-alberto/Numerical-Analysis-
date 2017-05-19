from eigen_values import Solver

solver = Solver("m_rar_sim_2017.txt")
#print(solver.generate_random_v0())


#not implemented
#print(solver.multiply_column_vector_with_line_vector([1, 2, 3], [1, 0, 1]))

# not implemented
#print(solver.multiply_normal_matrix_with_vector([[1, 0, 1], [2, 0, 2], [3, 0, 3]], [1, 2, 3]))
	# try: multiply_matrix_with_vector


#print(solver.find_largest_eigen_value(rand=True))
#print(solver.generate_svd_matrix())
solver.find_svd_eigen_values(10, 9)