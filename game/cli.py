def main():
	XO_FIELD_INITIAL = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	CHECK_WIN_FLAG = False
	WINNER = 'NOBODY'
	PLAYER = 'X'

	XO_field = XO_FIELD_INITIAL

	def validate_XO(xo):
		# 1) XO — это list
		if not isinstance(xo, list):
			raise TypeError("XO должен быть list")

		# 2) Размерность 9
		if len(xo) != 9:
			raise ValueError("Длина XO должна быть 9")

		# 3) Разрешены только числа или 'X'/'O'
		for i, v in enumerate(xo):
			if not (isinstance(v, int) or v in ('X', 'O')):
				raise ValueError(f"idx {i}: {v!r} — допустимы только int или 'X'/'O'")

		# 4) Числа на «своих» местах: i-й элемент равен i+1
		for i, v in enumerate(xo):
			if isinstance(v, int) and v != i + 1:
				raise ValueError(f"idx {i}: число должно быть {i+1}, а не {v}")

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
			
		MOVE_CORRECTNESS_FLAG = False
		while not MOVE_CORRECTNESS_FLAG:
			move_s = input("Type your choice: ").strip() 
			# to cut the move_s string from spaces and other invisible symbols
			if move_s.isdigit() and int(move_s) in xo:
				# to check that move_s is digit and is inside the xo list
				move = int(move_s)
				xo[move - 1] = player
				MOVE_CORRECTNESS_FLAG = True
				return xo
			else:
				print("incorrect input data. Please try again")
				print(player, "still moves")
			
			
	def check_win (xo: list):
		CHECK_WIN_FLAG = 0
		CHECK_WIN_FLAG_EXTERNAL = False
		WINNER = 'NOBODY'
		XO_FIELD_FULL = ['X', 'O']
		#check rows
		for i in range(0,6,3):
			if xo[i] == xo[i+1] and xo[i+1] == xo[i+2]:
				CHECK_WIN_FLAG = 1
				WINNER = xo[i]
		#check columns
		for j in range(0,3,1):
			if xo[j] == xo[j+3] and xo[j+3] == xo[j+6]:
				CHECK_WIN_FLAG = 1
				WINNER = xo[j]
		#check diafonals
		if xo[0] == xo[4] and xo[4] == xo[8]:
			CHECK_WIN_FLAG = 1
			WINNER = xo[4]
		if xo[2] == xo[4] and xo[4] == xo[6]:
			CHECK_WIN_FLAG = 1
			WINNER = xo[4]
		# draw check
		if all(x in XO_FIELD_FULL for x in xo):
			CHECK_WIN_FLAG = 2
			WINNER = 'FRIENDSHIP'
		if CHECK_WIN_FLAG == 1:
			print("Player ", WINNER, " won!!!")
			CHECK_WIN_FLAG_EXTERNAL = True		
		if CHECK_WIN_FLAG == 2:
			print("It is a draw!\n", WINNER, " won!!!")
			CHECK_WIN_FLAG_EXTERNAL = True
		return CHECK_WIN_FLAG_EXTERNAL

	
	while not CHECK_WIN_FLAG:
		try:
			validate_XO(XO_field)
		except (TypeError, ValueError) as e:
			print("Error while trying print field: ", e)
		
		print_field(XO_field)
		XO_field = make_a_move(PLAYER, XO_field)

		try:
			validate_XO(XO_field)
		except (TypeError, ValueError) as e:
			print("Error while trying print field: ", e)

		print_field(XO_field)	
		CHECK_WIN_FLAG = check_win(XO_field)
		PLAYER = change_side(PLAYER)
		
	

