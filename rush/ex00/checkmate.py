def checkmate(board):
    # 1. แปลง Input เป็น list ของแต่ละบรรทัด
    if isinstance(board, str):
        lines = [line for line in board.strip().split('\n') if line.strip()]
    elif isinstance(board, list):
        lines = [line.strip() for line in board if line.strip()]
    else:
        print("incorrect board")
        return

    # 2. ตรวจสอบความถูกต้องของตาราง (incorrect board)
    rows = len(lines)
    if rows == 0:
        print("incorrect board")
        return

    for row in lines:
        if len(row) != rows: # ขนาดแต่ละแถวต้องเท่ากับจำนวนแถว (สี่เหลี่ยมจัตุรัส NxN)
            print("incorrect board")
            return

    # 3. นับจำนวน King และหาตำแหน่ง
    king_r, king_c = -1, -1
    king_count = 0

    for r in range(rows):
        for c in range(rows):
            if lines[r][c] == 'K':
                king_r, king_c = r, c
                king_count += 1

    # ตรวจสอบจำนวน King (indefinite king)
    if king_count != 1:
        print("indefinite king")
        return

    # 4. เช็คการรุกจากทุกทิศทาง
    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1),   # ขึ้น, ลง, ซ้าย, ขวา (Rook, Queen)
        (-1, -1), (-1, 1), (1, -1), (1, 1)  # ทแยง 4 ทิศ (Bishop, Queen, Pawn)
    ]

    for dr, dc in directions:
        r, c = king_r + dr, king_c + dc
        step = 1

        while 0 <= r < rows and 0 <= c < rows:
            piece = lines[r][c]

            if piece != '.':
                # แนวตั้ง / แนวนอน
                if dr == 0 or dc == 0:
                    if piece in ('R', 'Q'):
                        print("Success")
                        return
                # แนวทแยง
                else:
                    if piece in ('B', 'Q'):
                        print("Success")
                        return
                    # Pawn (P) เดินเฉียงลงมา 1 ช่อง
                    if step == 1 and dr == 1 and piece == 'P':
                        print("Success")
                        return

                break # เจอหมากขวางทางแล้ว หยุดเช็คทิศนี้

            r += dr
            c += dc
            step += 1

    print("Fail")