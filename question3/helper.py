def binary_x(input_string, curr_string):
	if len(input_string) < 1:		
		print curr_string
		return curr_string

	curr_char = input_string[0]
	if curr_char == '1' or curr_char == '0':
		curr_string += curr_char
		remaining_string = input_string[1:]
		return binary_x(remaining_string, curr_string)
	elif curr_char == 'X' or curr_char == 'x':
		remaining_string = input_string[1:]
		x_0 = curr_string + '0'		
		x_1 = curr_string + '1'
		return binary_x(remaining_string, x_0) + binary_x(remaining_string, x_1)
	else:
		raise Exception("Invalid String - Example: 'python main.py 1X0XX' ")
		return