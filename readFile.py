def read_file(file_name):
	file = open(file_name, "r")
	lines = file.readlines()
	file.close()
	return lines