import random
import pygame

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # symbolic constants
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    # Before the loop: create speed variables
    speed_x = random.randint(-1,1)
    speed_y = random.randint(-1,1)
    size = (1000, 800)

    # intialize the Pygame engine
    pygame.init()

    # setup the screen
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Lord Julian RULeZ")
    # keep the animation loop going
    running = True
    # this is a Rect object in Pygame -- draw to the screen
    rect = pygame.Rect((size[0]-100)/2, (size[1]-100)/2, 100, 100)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #0-255 2^8 = RGB 0000 0000 1111 1111
        screen.fill(BLACK)
        pygame.draw.rect(screen, BLUE, rect)
        pygame.display.flip()
        # Update position (move the rect)
        rect.x += speed_x
        rect.y += speed_y

        if rect.x > size[0] or rect.x < 0:
            speed_x *= -1
        if rect.y > size[1] or rect.y < 0:
            speed_y *= -1

    pygame.quit()

