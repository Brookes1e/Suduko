



def draw(input_sudoku_2d):
    """
    draw function.
        Completes the GUI for the sudoku solver

    Parameters
    ----------
    input_sudoku_2d : [int,int]
        describes the current sudoku being solved, varing completed depending on the progression of the main() function
        in Sudoku_Solver.py
    """
    import pygame
    import itertools
    import time

    pygame.init()
    square_size = 50
    screen = pygame.display.set_mode((9 * square_size + 3, 9 * square_size + 3))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("comicsansms", 14)

    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        for x in range(9):
            spacing_x = 1
            if x % 3 == 0:
                spacing_x = 3

            for y in range(9):
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x * 50, y * 50, square_size, square_size))
                spacing_y = 1
                if y % 3 == 0:
                    spacing_y = 3

                pygame.draw.rect(screen, (255, 255, 255),
                                 pygame.Rect(x * 50 + spacing_x, y * 50 + spacing_y, square_size - spacing_x,
                                             square_size - spacing_y))

        for x_index, y_index in itertools.product(range(9),range(9)):
            text = font.render(str('%1d' % input_sudoku_2d[x_index][y_index]), True, (0, 0, 0))
            screen.blit(text,(x_index*square_size+(square_size/2),y_index*square_size+15))

        pygame.display.update()
        clock.tick(60)
        time.sleep(0.25)
        done = True

