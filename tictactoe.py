#create board
def create_board():
    board = []
    for i in range(3):
        board.append(['-','-','-'])
    #print(board)
    return board

#player 1
def player_1(board):

    print('row : ', end='')
    row = int(input())
    print('column : ', end='')
    column = int(input())


    #check if the location is already filled.
    #if filled , then print board and tell to select another location

    if -1 < row < 3 and -1 < column < 3 and board[row][column] == '-':
        board[row][column] = 'X'
    else:
        print('Sorry the location is already occupied or you have entered wrong location')
        board = player_1(board)
    return board

#player 2
def player_2(board):
    print('row : ', end='')
    row = int(input())
    print('column : ', end='')
    column = int(input())

     #check if the location is already filled.
    #if filled , then print board and tell to select another location
    
    if -1 < row < 3 and -1 < column < 3 and board[row][column] == '-':
        board[row][column] = 'O'
    else:
        print('Sorry the location is already occupied or you have entered wrong location')
        board = player_2(board)
    return board

#check status of board
    #status 1 - win : A player has won game
    #status 2 - draw : the board is full and no one won
    #status 3 - next_turn : game continues

def check_board(board,symbol):
    #check if a player won
    win = [symbol,symbol,symbol]
    #check rows
    for i in range(3):
        if board[i] == win:
            return 'win'
    
    #check columns
    for i in range(3):
        col = []
        for j in range(3):
            col.append(board[j][i])
        
        if col == win:
            return 'win'
    
    #check diagonal
    diagonal_1 = [board[0][0],board[1][1],board[2][2]]
    diagonal_2 = [board[0][2],board[1][1],board[2][0]]

    if diagonal_1 == win or diagonal_2 == win:
        return 'win'
                
    #check if the board is full
    for i in range(len(board)):
        for j in range(len(board[i])):
            if(board[i][j]) == '-':
                print('over to next player')
                return 'next_turn'
    
    return 'draw'


#print board
def print_board(board):
    print('Printing board')
    for i in range(3):
        print('{0} {1} {2}'.format(board[i][0],board[i][1],board[i][2]))

#start_game
def start_game():
    board = create_board()
    turn = 1
    while(True):
        print('value of turn = ', turn)
        if turn%2 == 1:
            print('player 1 turn : ')
            board = player_1(board)
            status = check_board(board,'X')
            if status == 'win':
                print("Well played. Player 1 won, Player 2 lost")
                print_board(board)
                break

            elif status == 'draw':
                print("Well played. The game ended in a draw")
                print_board(board)
                break
            else:
                print('next turn ' + '*****'*10)

        else:
            print('player 2 turn : ')
            board = player_2(board)
            status = check_board(board,'O')
            if status == 'win':
                print("Well played. Player 2 won, Player 1 lost")
                print_board(board)
                break

            elif status == 'draw':
                print("Well played. The game ended in a draw")
                print_board(board)
                break

            else:
                print('next turn ' + '*****'*10)
        
        print_board(board)
        turn = turn + 1

    print('Thank you for playing')


start_game()