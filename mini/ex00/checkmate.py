# ---------- สัญลักษณ์ตัวหมาก ----------
KING   = "K"  
QUEEN  = "Q" 
BISHOP = "B"
ROOK   = "R"
PAWN   = "P"

# ตัวอักษรที่ "นับเป็นหมาก" จริง ๆ นอกจากนี้ถือเป็นช่องว่างทั้งหมด
PIECES = (KING, QUEEN, BISHOP, ROOK, PAWN)

# 8 ทิศที่จะยิงรังสีออกจาก King
STRAIGHT_DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))      # บน ล่าง ซ้าย ขวา
DIAGONAL_DIRS = ((-1, -1), (-1, 1), (1, -1), (1, 1))    # ทแยง 4 มุม


def parse_board(board):
    """แปลง string ของกระดานเป็น list ของแถว + ตรวจความถูกต้อง"""
    if not isinstance(board, str):
        raise TypeError("board must be a string") #ส่งค่า error ถ้า board ไม่ใช่ string

    rows = board.split("\n") # เก็บข้อมูลกระดานเป็น list ของ string แต่ละบรรทัด (แถว) โดยตัด newline ออก

    # ตัดบรรทัดว่างท้ายสุดทิ้ง (เผื่อ string ลงท้ายด้วย newline)
    while rows and rows[-1] == "": #ทำซ้ำจนกว่าจะเจอบรรทัดไม่ว่าง หรือ list ว่าง
        rows.pop() # ตัดบรรทัดว่างท้ายสุด

    if not rows:
        raise ValueError("board is empty") #ส่งค่า error ถ้าไม่มีบรรทัดใด ๆ

    size = len(rows)
    for row in rows:
        if len(row) != size:
            raise ValueError("board must be a square")

    return rows


def find_king(rows):
    """หาตำแหน่ง King และยืนยันว่ามีตัวเดียวจริง ๆ"""
    position = None
    for r, row in enumerate(rows): #ทำซ้ำแต่ละแถวของกระดาน (r = index ของแถว, row = string ของแถวนั้น)
        for c, square in enumerate(row): #ทำซ้ำแต่ละช่องของแถว (c = index ของช่อง, square = ตัวอักษรในช่องนั้น)
            if square == KING:
                if position is not None: 
                    raise ValueError("more than one king on the board")
                position = (r, c) #เก็บตำแหน่งของ King เป็น tuple (แถว, คอลัมน์)

    if position is None:
        raise ValueError("no king on the board")
    return position


def first_piece_in_direction(rows, start, direction):
    """
    เดินจากช่อง start ไปทางทิศ direction ทีละช่อง
    คืนค่า (ตัวหมากตัวแรกที่เจอ, ระยะห่างกี่ช่อง)
    ถ้าเดินจนตกขอบกระดานโดยไม่เจอใคร -> (None, 0)
    """
    size = len(rows)
    dr, dc = direction
    r, c = start[0] + dr, start[1] + dc
    distance = 1

    while 0 <= r < size and 0 <= c < size:
        square = rows[r][c]
        if square in PIECES:          # เจอหมากตัวแรก = หยุดทันที (มันบังทาง)
            return square, distance
        r += dr
        c += dc
        distance += 1

    return None, 0


def is_in_check(rows, king):
    """เช็คว่า King ที่ตำแหน่ง king กำลังถูกรุกหรือไม่"""

    # --- ทิศตรง: Rook กับ Queen กินได้ ---
    for direction in STRAIGHT_DIRS:
        piece, _ = first_piece_in_direction(rows, king, direction)
        if piece in (ROOK, QUEEN):
            return True

    # --- ทิศทแยง: Bishop, Queen และ Pawn (ระยะ 1 ช่อง) ---
    for direction in DIAGONAL_DIRS:
        piece, distance = first_piece_in_direction(rows, king, direction)
        if piece in (BISHOP, QUEEN):
            return True
        # Pawn กินทแยงไปข้างหน้า (แถวน้อยลง) => อยู่ "ใต้" King พอดี 1 ช่อง
        if piece == PAWN and distance == 1 and direction[0] == 1:
            return True

    return False


def checkmate(board):
    """ฟังก์ชันหลักตามโจทย์: พิมพ์ Success ถ้าถูกรุก, Fail ถ้าไม่ถูกรุก"""
    try:
        rows = parse_board(board)
        king = find_king(rows)
    except (TypeError, ValueError) as error:
        print("Error: {}".format(error))
        return

    print("Success" if is_in_check(rows, king) else "Fail")