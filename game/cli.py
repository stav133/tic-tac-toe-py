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

	    
	# keep in cli as is
	def print_field(xo: list):
		print("+-----+-----+-----+")
		print("|-", xo[0], "-|-", xo[1], "-|-", xo[2], "-|")
		print("|-", xo[3], "-|-", xo[4], "-|-", xo[5], "-|")
		print("|-", xo[6], "-|-", xo[7], "-|-", xo[8], "-|")
		print("+-----+-----+-----+")


	# keep in cli as is
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


	
	def read_move_input (player: str) -> str:
		move_s = input("Type your choice: ").strip() 
		return move_s
		
		
	def parse_and_validate_move (move_s: str, xo:list) -> int | None:
		if move_s.isdigit():
			move = int(move_s)
			if move in xo:
				return move
			return None
			
	
	def apply_move (xo: list, move: int, player: str) -> None:
		xo[move-1] = player


	def make_a_move (player: str, xo:list):
		# check that player has correct value (X or O)
		if player not in ('X', 'O'):
			print("Field PLAYER in funtion make_a_move has incorrect value")
			return
		print(player, "moves")
			
		while True:
			move_s = read_move_input(player)
			move = parse_and_validate_move(move_s, xo)
			if move is not None:
				apply_move (xo, move, player)
				return xo, move
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

	
#	def update_xo_with_counter(xo:list, saver):
	
	
	THRESHOLD = 5
	counter = 1
	saver = [999] * THRESHOLD
	move = 999
	
	while not check_win_flag:
		try:
			validate_xo(xo_field)
		except (TypeError, ValueError) as e:
			print("Error while trying print field: ", e)
		
		print("Move: ", counter)
		print_field(xo_field)
		xo_field, move = make_a_move(player, xo_field)

		try:
			validate_xo(xo_field)
		except (TypeError, ValueError) as e:
			print("Error while trying print field: ", e)

		
		check_win_flag = check_win(xo_field)
		
		if check_win_flag:
			print_field(xo_field)
		else:
			if counter > THRESHOLD:
				xo_field[saver[0]-1] = saver[0]
				for i in range(0, THRESHOLD-1, 1):
					saver[i] = saver[i+1]
				saver[THRESHOLD-1] = move
			if counter <= THRESHOLD:
				saver[counter-1] = move
					
			player = change_side(player)
			
			counter = counter + 1

