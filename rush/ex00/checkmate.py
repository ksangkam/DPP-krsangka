PIECES = "KPBRQ"

ROOK_DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
BISHOP_DIRS = [(-1, -1), (-1, 1), (1, -1), (1, 1)]


def parse_board(board):

    if not isinstance(board, str):
        return None

    rows = board.splitlines()
    size = len(rows)

    if size == 0:
        return None

    # Check the board it if is a square
    for row in rows:
        if len(row) != size:
            return None

    # ต้องมี King ตัวเดียวเท่านั้น
    king_count = sum(row.count("K") for row in rows)
    if king_count != 1:
        return None

    return rows


def find_king(rows):
    for r, row in enumerate(rows):
        c = row.find("K")
        if c != -1:
            return r, c
    return None


def first_piece(rows, r, c, dr, dc):
    """เดินจากตำแหน่ง (r, c) ไปตามทิศ (dr, dc)
    คืนตัวหมากตัวแรกที่เจอ หรือ None ถ้าไม่เจอจนสุดกระดาน"""
    size = len(rows)
    r += dr
    c += dc
    while 0 <= r < size and 0 <= c < size:
        if rows[r][c] in PIECES:
            return rows[r][c]
        r += dr
        c += dc
    return None


def is_in_check(rows):
    size = len(rows)
    kr, kc = find_king(rows)


    pr = kr + 1
    if pr < size:
        for pc in (kc - 1, kc + 1):
            if 0 <= pc < size and rows[pr][pc] == "P":
                return True

    # Rook / Queen: แนวตรง
    for dr, dc in ROOK_DIRS:
        if first_piece(rows, kr, kc, dr, dc) in ("R", "Q"):
            return True

    # Bishop / Queen: แนวเฉียง
    for dr, dc in BISHOP_DIRS:
        if first_piece(rows, kr, kc, dr, dc) in ("B", "Q"):
            return True

    return False


def checkmate(board):
    rows = parse_board(board)
    if rows is None:
        print("Error")
        return

    if is_in_check(rows):
        print("Success")
    else:
        print("Fail")