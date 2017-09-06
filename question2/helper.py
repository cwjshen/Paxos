def find_pair(item_list, gift_card):

	# Invalid inputs
	if not item_list or len(item_list) < 2:
		raise Exception('Not Possible - Invalid text file')
	else:

		# Pointers to navigate list
		head_index = 0
		tail_index = len(item_list) - 1 

		# Keep track of maximum spending
		max_item_sum = 0

		# Algorithm - See solutions.txt
		while (head_index < tail_index):
			item_sum = item_list[head_index][1] + item_list[tail_index][1]

			if item_sum == gift_card:
				gift_1 = item_list[head_index]
				gift_2 = item_list[tail_index]
				# Solution
				return (gift_1, gift_2)				
				
			elif item_sum > gift_card:
				tail_index -= 1
			else:
				if item_sum > max_item_sum:
					max_item_sum = item_sum
					gift_1 = item_list[head_index]
					gift_2 = item_list[tail_index]
					gifts = (gift_1, gift_2)
				head_index += 1

		
		if max_item_sum == 0:
			raise Exception('Not Possible')

		# Solution
		return (gift_1, gift_2)

def find_triple(item_list, gift_card):

	# Invalid inputs
	if not item_list or len(item_list) < 3:
		raise Exception('Not Possible - Invalid text file')
	else:		

		# Keep track of maximum spending
		max_item_sum = 0

		# Initialize gifts
		gift1 = None
		gift2 = None
		gift3 = None

		# Algorithm - See solutions.txt
		for i in range(len(item_list) - 2):
			item1 = item_list[i]

			# Create remaining list
			remaining_list = list(item_list)
			del remaining_list[i]			

			item2, item3 = find_pair(remaining_list, gift_card - item1[1])	
			item_sum = item1[1] + item2[1] + item3[1]

			if item_sum == gift_card:
				return (item1, item2, item3)
			elif item_sum > gift_card:
				continue
			else:
				if item_sum > max_item_sum:
					max_item_sum = item_sum
					gift1, gift2, gift3 = (item1, item2, item3)

		# If no solutions were found
		if max_item_sum == 0:
			raise Exception('Not Possible')

		# Solution
		return (gift1, gift2, gift3)		