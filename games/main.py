import pygame

if __name__ == '__main__':
    try:
        pygame.init()
        size = [int(x) for x in input().split()]
        RED = (255, 0, 0)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption('Прямоугольник')
        pygame.draw.rect(screen, RED, (1, 1, size[0] - 2, size[1] - 2), width=0)

        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()
    except ValueError:
        print('Неправильный формат ввода')