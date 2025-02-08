def is_safe(row, col):
    for r, c in enumerate(partial):
        # No esta en la misma columna o diagonales
        # No es necesario verificar la fila debido a la forma en que se construye la solucion
        if c == col or (r + c == row + col) or (r - c == row - col):
            return False
    return True

def backtrack(row):
    if row == 8:
        return 1
    
    ways = 0
    for col in range(8):
        if board[row][col] == '.':
            # Si es posible exploramos solucion colocando reina en esa columna
            if is_safe(row, col):
                partial.append(col)
                ways += backtrack(row + 1)
                partial.pop()
    return ways

board = [input().strip() for _ in range(8)]
partial = [] 
res = backtrack(0)

print(res)