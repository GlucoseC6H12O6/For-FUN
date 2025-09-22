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
    
    
def route_recoder (route, present_position) :
    route.append(present_position)
    return route

def check_success(chess_board):
    for row in chess_board:
        for cell in row:
            if cell == "O": 
                return False
    return True

def choose_move_warnsdorff(chess_board, present):
    candidates = knignt_next_position(chess_board, present)
    if not candidates:
        return None

    # 동률 깨기 위해 섞고 -> 차수 최소인 걸 선택
    random.shuffle(candidates)

    def degree(pos):
        # 해당 후보 칸에서 갈 수 있는 다음 "O"의 개수
        return len(knignt_next_position(chess_board, pos))

    return min(candidates, key=degree)

# [NEW] 특정 좌표로 나이트를 이동(랜덤 선택 없이 목적지 고정)
def move_knight_to(chess_board, present_position, where):
    y1, x1 = present_position
    y2, x2 = where
    chess_board[y1][x1] = "X"
    chess_board[y2][x2] = "♞"
            
def knights_tour_warnsdorff():
    chess_board = init_chess()
    route = []

    # 시작 지점
    present_position = knight_present_position(chess_board)
    route = route_recoder(route, present_position)

    # 첫 이동 후보 선택
    where = choose_move_warnsdorff(chess_board, present_position)
    if where is None:
        # 시작에서부터 막힘
        print("Knight's Journey is Over (Warnsdorff)")
        print("Footsteps of a Knight", route)
        print_chess(chess_board)
        print("경로 길이:", len(route))
        print("실패! 모든 칸을 방문하지 못했습니다.")
        return False

    move_knight_to(chess_board, present_position, where)

    # 반복
    while True:
        present_position = knight_present_position(chess_board)
        route = route_recoder(route, present_position)

        where = choose_move_warnsdorff(chess_board, present_position)
        if where is None:
            break

        move_knight_to(chess_board, present_position, where)
    
    print_chess(chess_board)
    print("경로 길이:", len(route))
    if check_success(chess_board):
        print("성공! 나이트가 모든 칸을 방문했습니다.")
        print("Footsteps of a Knight", route)
        print_chess(chess_board)
        return True
    else:
        print("실패! 모든 칸을 방문하지 못했습니다.")
        return False
    
attempt = 0
while True:
    attempt += 1
    print(f"\n===== Warnsdorff 시도 {attempt} =====")
    if knights_tour_warnsdorff():
        print(f"🎉 {attempt}번째 시도에서 성공!")
        break
    if attempt > 100: break