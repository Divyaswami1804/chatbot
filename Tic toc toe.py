import pygame

pygame.init()

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("X O GAME")

White = (255,255,255)
black = (0,0,0)
neon = (0, 200, 255)
size = 200

board = [["", "", ""],
         ["", "", ""],
         ["", "", ""]]

player = "X"
font = pygame.font.Font(None, 100)
run = True

def winner():
    for r in range(3):
        if board[r][0] == board[r][1] == board[r][2] != "":
            return True
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] != "":
            return True
    if board[0][0] == board[1][1] == board[2][2] != "":
        return True
    if board[0][2] == board[1][1] == board[2][0] != "":
        return True
    return False


def draw_outline_text(text, x, y):
    outline_font = pygame.font.Font(None, 120)
    main_font = pygame.font.Font(None, 110)

    outline_layers = [(-3,-3),(-3,3),(3,-3),(3,3)]
    for ox, oy in outline_layers:
        t = outline_font.render(text, True, neon)
        screen.blit(t, (x+ox, y+oy))

    main_text = main_font.render(text, True, black)
    screen.blit(main_text, (x, y))

while run:
    screen.fill(White)

    pygame.draw.line(screen, black, (200,0), (200,600),5)
    pygame.draw.line(screen, black, (400,0), (400,600),5)
    pygame.draw.line(screen, black, (0,200), (600,200),5)
    pygame.draw.line(screen, black, (0,400), (600,400),5)

    for row in range(3):
        for col in range(3):
            if board[row][col] != "":
                text = font.render(board[row][col], True, black)
                screen.blit(text, (col*size + 70, row*size + 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            row = mouse_y // size
            col = mouse_x // size

            if board[row][col] == "":
                board[row][col] = player

                if winner():
                    winner_text = f"{player} WINS!"
                    while True:
                        screen.fill(White)

                        pygame.draw.line(screen, black, (200,0), (200,600),5)
                        pygame.draw.line(screen, black, (400,0), (400,600),5)
                        pygame.draw.line(screen, black, (0,200), (600,200),5)
                        pygame.draw.line(screen, black, (0,400), (600,400),5)

                        for r in range(3):
                            for c in range(3):
                                if board[r][c] != "":
                                    t = font.render(board[r][c], True, black)
                                    screen.blit(t, (c*size + 70, r*size + 50))

                        draw_outline_text(winner_text, 120, 230)
                        pygame.display.update()

                        for e in pygame.event.get():
                            if e.type == pygame.QUIT:
                                pygame.quit()
                                exit()

                player = "O" if player == "X" else "X"

    pygame.display.update()

pygame.quit()
