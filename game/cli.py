def main():
	xo_field_initial = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	check_win_flag = False
	winner = 'NOBODY'
	player = 'X'

	xo_field = xo_field_initial

	def validate_xo(xo):
		# to check that xo is list type
		if not isinstance(xo, list):
			raise TypeError("xo must be list")

		# to check that dimension is 9
		if len(xo) != 9:
			raise ValueError("The length of xo must be 9")

		# to check that only digits or 'X'/'O' are available
		for i, v in enumerate(xo):
			if not (isinstance(v, int) or v in ('X', 'O')):
				raise ValueError(f"idx {i}: {v!r} — could be only int or 'X'/'O'")

		# to check that digits are on correct places: i-th element equals i+1
		for i, v in enumerate(xo):
			if isinstance(v, int) and v != i + 1:
				raise ValueError(f"idx {i}: digit must be {i+1}, but not {v}")

		return True
	    
	def print_field(xo: list):
		print("+-----+-----+-----+")
		print("|-", xo[0], "-|-", xo[1], "-|-", xo[2], "-|")
		print("|-", xo[3], "-|-", xo[4], "-|-", xo[5], "-|")
		print("|-", xo[6], "-|-", xo[7], "-|-", xo[8], "-|")
		print("+-----+-----+-----+")


	def change_side(player):
		# check that player has correct value (X or O)
		if not player in ('X', 'O'):
			print("Field PLAYER in funtion change_side has incorrect value")
			return
		if player == 'X':
			player = 'O'
			return player
		if player == 'O':
			player = 'X'
			return player


	def make_a_move (player, xo:list):
		# check that player has correct value (X or O)
		if not player in ('X', 'O'):
			print("Field PLAYER in funtion make_a_move has incorrect value")
			return
		print(player, "moves")
			
		move_correctness_flag = False
		while not move_correctness_flag:
			move_s = input("Type your choice: ").strip() 
			# to cut the move_s string from spaces and other invisible symbols
			if move_s.isdigit() and int(move_s) in xo:
				# to check that move_s is digit and is inside the xo list
				move = int(move_s)
				xo[move - 1] = player
				move_correctness_flag = True
				return xo
			else:
				print("incorrect input data. Please try again")
				print(player, "still moves")
			
			
	def check_win (xo: list):
		check_win_flag = 0
		check_win_flag_external = False
		winner = 'NOBODY'
		xo_field_full = ['X', 'O']
		#check rows
		for i in range(0,6,3):
			if xo[i] == xo[i+1] and xo[i+1] == xo[i+2]:
				check_win_flag = 1
				winner = xo[i]
		#check columns
		for j in range(0,3,1):
			if xo[j] == xo[j+3] and xo[j+3] == xo[j+6]:
				check_win_flag = 1
				winner = xo[j]
		#check diafonals
		if xo[0] == xo[4] and xo[4] == xo[8]:
			check_win_flag = 1
			winner = xo[4]
		if xo[2] == xo[4] and xo[4] == xo[6]:
			check_win_flag = 1
			winner = xo[4]
		# draw check
		if all(x in xo_field_full for x in xo):
			check_win_flag = 2
			winner = 'FRIENDSHIP'
		if check_win_flag == 1:
			print("Player ", winner, " won!!!")
			check_win_flag_external = True		
		if check_win_flag == 2:
			print("It is a draw!\n", winner, " won!!!")
			check_win_flag_external = True
		return check_win_flag_external

	
	while not check_win_flag:
		try:
			validate_xo(xo_field)
		except (TypeError, ValueError) as e:
			print("Error while trying print field: ", e)
		
		print_field(xo_field)
		xo_field = make_a_move(player, xo_field)

		try:
			validate_xo(xo_field)
		except (TypeError, ValueError) as e:
			print("Error while trying print field: ", e)

		print_field(xo_field)	
		check_win_flag = check_win(xo_field)
		player = change_side(player)
		
	

