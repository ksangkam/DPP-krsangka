def checkmate(board):
    if isinstance(board, str):
        lines = [line for line in board.strip().split('\n') if line.strip()]
    elif isinstance(board, list):
        lines = [line.strip() for line in board if line.strip()]
    else:
        print("incorrect board")
        return

    size = len(lines)
    if size == 0:
        print("incorrect board")
        return

    for row in lines:
        if len(row) != size:
            print("incorrect board")
            return

    king_r, king_c = -1, -1
    king_count = 0
    for r in range(size):
        for c in range(size):
            if lines[r][c] == 'K':
                king_r, king_c = r, c
                king_count += 1

    if king_count != 1:
        print("indefinite king")
        return

    def is_clear_path(r1, c1, r2, c2):
        dr = (r2 > r1) - (r2 < r1)
        dc = (c2 > c1) - (c2 < c1)
        
        curr_r, curr_c = r1 + dr, c1 + dc
        while (curr_r, curr_c) != (r2, c2):
            if lines[curr_r][curr_c] != '.':
                return False
            curr_r += dr
            curr_c += dc
        return True

    for r in range(size):
        for c in range(size):
            piece = lines[r][c]
            
            diff_r = abs(r - king_r)
            diff_c = abs(c - king_c)

            if piece == 'P':
                if r - king_r == 1 and diff_c == 1:
                    print("Success")
                    return

            if piece in ('R', 'Q'):
                if (r == king_r or c == king_c) and (r, c) != (king_r, king_c):
                    if is_clear_path(r, c, king_r, king_c):
                        print("Success")
                        return

            if piece in ('B', 'Q'):
                if diff_r == diff_c and diff_r > 0:
                    if is_clear_path(r, c, king_r, king_c):
                        print("Success")
                        return

    print("Fail")