import random
def init_chess() :
    chess_board = []
    for i in range(0,8) :
        chess_board.append([])
        for k in range(0,8) :
            if ((i == 7) and (k ==0)) :
                chess_board[i].append("♞")
            else :
                chess_board[i].append("O")
    return chess_board

def print_chess(chess_board) :
    for i in range(0,8) :
        for k in range(0,8) :
            print(chess_board[i][k],end=' ')
        print("")
        
def knight_present_position(chess_board) :
    for i in range(0,8) :
        for k in range(0,8) :
            if chess_board[i][k] == "♞" :
                return [i, k]
            else :
                continue  
            
def knignt_next_position(chess_board, present) :
    moves = [
        [present[0]+2, present[1]+1], [present[0]+2, present[1]-1],
        [present[0]-2, present[1]+1], [present[0]-2, present[1]-1],
        [present[0]+1, present[1]+2], [present[0]+1, present[1]-2],
        [present[0]-1, present[1]+2], [present[0]-1, present[1]-2]]
    next_position = []
    for i in range(0,len(moves)) :
        y = moves[i][0]
        x = moves[i][1]
        if ((y in range(0,8)) and (x in range(0,8))) :
            if chess_board[y][x] == "O" :
                next_position.append(moves[i])
        else :
            continue
    return next_position
    
def move_knight (chess_board, present_position, next_position) :
    where = random.choice(next_position)
    y1 = present_position[0]
    x1 = present_position[1]
    y2 = where[0]
    x2 = where[1]
    
    chess_board[y1][x1] = "X"
    chess_board[y2][x2] = "♞"
    
def route_recoder (route, present_position) :
    route.append(present_position)
    return route

def check_success(chess_board):
    for row in chess_board:
        for cell in row:
            if cell == "O": 
                return False
    return True
            
def knights_tour () :
    chess_board = init_chess()
    route = []
    present_position = knight_present_position(chess_board)
    route = route_recoder(route, present_position)
    next_position = knignt_next_position(chess_board, present_position)
    move_knight(chess_board,present_position, next_position)

    while True:
        present_position = knight_present_position(chess_board)
        route = route_recoder(route, present_position)
        next_position = knignt_next_position(chess_board, present_position)

        if len(next_position) == 0:  
            break

        move_knight(chess_board, present_position, next_position)

    print("Route Length:", len(route))
    if check_success(chess_board):
        print("Knight's Tour Success.\n")
        print_chess(chess_board)
        print("Footsteps of a Knight {0}".format(route))
        return True
    else:
        print("Knight's Tour Fail.\n")
        return False
        
for i in range(0,1000000) :
    print("Attemp {0}".format(i))
    result = knights_tour()
    if result == True :
        break
    else :
        continue