def read_board(file_path):
    board = []

    # doc file 
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if len(line) != 3 or any(key not in 'XO.' for key in line):
                print('Invalid board !!')
                exit()
            board.append(list(line))

    if len(board) != 3:
        print('Invalid board !!')
        exit()

    return board

# check x thang hoac o thang
def check_winner(board, player):
    # check hang, cot, duong cheo
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):  # hang
            return True
        if all(board[j][i] == player for j in range(3)):  # cot
            return True

    # duong cheo
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False
   
def is_valid_board(board):
    flat = [cell for row in board for cell in row]
    x_count = flat.count('X')
    o_count = flat.count('O')

    # check so luong x ma khong bang hoac lon hon so luong o 1 don vi -> false
    if not (x_count == o_count or x_count == o_count + 1):
        return False

    x_win = check_winner(board, 'X')
    o_win = check_winner(board, 'O')

    # check khong co 2 nguoi thang cung luc
    if x_win and o_win:
        return False

    # if x thang -> x_count = o_count + 1
    if x_win and x_count != o_count + 1:
        return False

    # if o thang -> o_count = o_count
    if o_win and x_count != o_count:
        return False

    return True

def is_full(board):
    for row in board:
        for cell in row:
            if cell == '.':
                return False
    
    return True

def minimax(board, is_maximizing, alpha, beta, depth):
    if check_winner(board, 'X'):
        return 1, depth
    if check_winner(board, 'O'):
        return -1, depth
    if is_full(board):
        return 0, depth

    if is_maximizing:
        max_eval = float('-inf')
        best_depth = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '.':
                    board[i][j] = 'X'
                    eval, d = minimax(board, False, alpha, beta, depth + 1)
                    board[i][j] = '.'

                    if eval > max_eval or (eval == max_eval and d < best_depth):
                        max_eval = eval
                        best_depth = d

                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval, best_depth
    else:
        min_eval = float('inf')
        best_depth = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '.':
                    board[i][j] = 'O'
                    eval, d = minimax(board, True, alpha, beta, depth + 1)
                    board[i][j] = '.'

                    if eval < min_eval or (eval == min_eval and d < best_depth):
                        min_eval = eval
                        best_depth = d

                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval, best_depth

def best_move(board):
    best_score = float('-inf')
    best_depth = float('inf')
    move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == '.':
                board[i][j] = 'X'
                score, depth = minimax(board, False, float('-inf'), float('inf'), 0)
                board[i][j] = '.'

                # uu tien score cao nhat, neu bang nhau -> chon depth lon hon
                # if score > best_score or (score == best_score and depth > best_depth):
                if score > best_score or (score == best_score and depth > best_depth):
                    best_score = score
                    best_depth = depth
                    move = (i, j)

    print(f"Best move is: {move} with score: {best_score}, depth: {best_depth}")
    return move


def main():
    file_path = './testcase/testcase1.txt'  
    # file_path = './testcase/testcase2.txt'  
    # file_path = './testcase/testcase3.txt'  
    # file_path = './testcase/testcase4.txt'  

    board = read_board(file_path)

    # ktra tinh hop le
    if not is_valid_board(board):
        print('Invalid board')
        return

    # check game over
    if check_winner(board, 'X') or check_winner(board, 'O') or is_full(board):
        print('Game over')
        return

    move = best_move(board)
    print(move)  


if __name__ == '__main__':
    main()

