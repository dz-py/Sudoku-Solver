import pygame

# Initialize the pygame library
pygame.init()

# Set up drawing window
length, width = 500, 620
window = pygame.display.set_mode((length, width))
pygame.display.set_caption("Sudoku Solver Using Backtracking Algorithm")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
light_grey = (211, 211, 211)
blue = (0, 0, 255)

# Fonts
font1 = pygame.font.SysFont("arial", 50)
font2 = pygame.font.SysFont("sans-serif", 30)

# Default Sudoku Board
board = [
     [7, 8, 0, 4, 0, 0, 1, 2, 0],
     [6, 0, 0, 0, 7, 5, 0, 0, 9],
     [0, 0, 0, 6, 0, 1, 0, 7, 8],
     [0, 0, 7, 0, 4, 0, 2, 6, 0],
     [0, 0, 1, 0, 5, 0, 9, 3, 0],
     [9, 0, 4, 0, 6, 0, 0, 0, 5],
     [0, 7, 0, 3, 0, 0, 0, 1, 2],
     [1, 2, 0, 0, 0, 7, 4, 0, 0],
     [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

gap = length / 9
x = 0
y = 0


def draw_window():
    window.fill(white)

    # Input The Numbers From Default Board
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                # Color The Input Cell
                pygame.draw.rect(window, light_grey, (j * gap, i * gap, gap + 1, gap + 1))

                # Input Default Board Into Grid
                text1 = font1.render(str(board[i][j]), True, black)
                window.blit(text1, (j * gap + 10, i * gap + 5))

    # Draw Sudoku Grid
    for i in range(10):
        if i % 3 == 0:
            thickness = 5
        else:
            thickness = 1
        pygame.draw.line(window, black, (0, i * gap), (500, i * gap), thickness)
        pygame.draw.line(window, black, (i * gap, 0), (i * gap, 500), thickness)

    # Directions
    text1 = font2.render("Press 'C' to clear and 'D' for default.", True, blue)
    text2 = font2.render("Input values and press 'Enter' to solve.", True, blue)
    text3 = font2.render("Or press 'Enter' to solve the default board.", True, blue)
    window.blit(text1, (10, 520))
    window.blit(text2, (10, 550))
    window.blit(text3, (10, 580))
    pygame.display.update()


# Fill Cell With Input Values
def fill_input(key):
    text = font1.render(str(key), True, black)
    window.blit(text, (x, y))


def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j


def valid(board, num, pos):
    # Check Row
    for i in range(9):
        if board[pos[0]][i] == num:
            return False

    # Check Column
    for i in range(9):
        if board[i][pos[1]] == num:
            return False

    # Check 3x3 Grids
    x_grid = (pos[0] // 3) * 3
    y_grid = (pos[1] // 3) * 3

    for i in range(3):
        for j in range(3):
            if board[x_grid + i][y_grid + j] == num:
                return False

    return True


def solve(board):
    pos = find_empty(board)
    if pos is None:
        return True

    for i in range(1, len(board) + 1):
        if valid(board, i, pos):
            board[pos[0]][pos[1]] = i
            if solve(board):
                return True
            board[pos[0]][pos[1]] = 0
    return False


key = 0
def main():
    run = True
    global key, board, x, y
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # Input
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                x = mouse_x // gap
                y = mouse_y // gap
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_RETURN:
                    solve(board)
                if event.key == pygame.K_c:
                    board = [
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0]
                    ]
                if event.key == pygame.K_d:
                    board = [
                         [7, 8, 0, 4, 0, 0, 1, 2, 0],
                         [6, 0, 0, 0, 7, 5, 0, 0, 9],
                         [0, 0, 0, 6, 0, 1, 0, 7, 8],
                         [0, 0, 7, 0, 4, 0, 2, 6, 0],
                         [0, 0, 1, 0, 5, 0, 9, 3, 0],
                         [9, 0, 4, 0, 6, 0, 0, 0, 5],
                         [0, 7, 0, 3, 0, 0, 0, 1, 2],
                         [1, 2, 0, 0, 0, 7, 4, 0, 0],
                         [0, 4, 9, 2, 0, 6, 0, 0, 7]
                    ]

        if key != 0:
            fill_input(key)
            board[int(y)][int(x)] = key
            key = 0
        draw_window()


main()
pygame.quit()
