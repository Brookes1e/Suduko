import eztext
import pygame


def main():
    pygame.init()
    square_size = 50
    screen = pygame.display.set_mode((9 * square_size + 3, 9 * square_size + 3))
    done = False
    txtbx = eztext.Input(maxlength=45, color=(0, 0, 0), prompt='type here: ')
    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            events = pygame.event.get()
            txtbx.update(events)
            txtbx.draw(screen)


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

        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':main()