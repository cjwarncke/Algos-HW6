from queue import Queue


def find_neighbors(puzzle, square):
    row, column = square
    neighbors = []
    # Check left
    if column > 0:
        if puzzle[row][column-1] == '-':
            neighbors.append((row, column-1))

    # Check right
    if column < len(puzzle[0]) - 1:
        if puzzle[row][column+1] == '-':
            neighbors.append((row, column+1))

    # Check up
    if row > 0:
        if puzzle[row-1][column] == '-':
            neighbors.append((row-1, column))

    # Check down
    if row < len(puzzle) - 1:
        if puzzle[row+1][column] == '-':
            neighbors.append((row+1, column))
    return neighbors


def solve_puzzle(board, source, destination):
    q = Queue(maxsize=len(board)*len(board[0]))
    visited = {source:None}
    q.put(source)
    while not q.empty() and destination not in visited:
        curr_square = q.get()
        neighbors = find_neighbors(board, curr_square)
        for neighbor in neighbors:
            if neighbor not in visited:
                visited[neighbor] = curr_square
                q.put(neighbor)


    # Trace solution path
    if destination not in visited:
        return None
    path = [destination]
    curr_square = destination
    while visited[curr_square] is not None:
        parent = visited[curr_square]
        path.append(parent)
        curr_square = parent
    path.reverse()
    return path
